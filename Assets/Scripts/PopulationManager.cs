using TMPro;
using UnityEngine;

public class PopulationManager : MonoBehaviour {

    public Vector2Int nPopulation = new(10, 10);
    public Vector2Int gridSize = new(20, 20);
    public int offset = 10;
    public GameObject cityPrefab;
    public DataReciever reciever;

    public TMP_Text generationText;
    public int generation = 1;

    [HideInInspector] public CityManager[] population;
    [HideInInspector] public CityManager selectedCity;
    public StateManager mainStateManager;

    private int episode = 0;
    public int maxEpisodes = 400;

    // Start is called before the first frame update
    void Start() {
        generationText.text = generation.ToString();
        // Create Population
        population = new CityManager[nPopulation.x * nPopulation.y];
        for(int i = 0; i < nPopulation.x; i++){
            for(int j = 0; j < nPopulation.y; j++){
                Vector3 pos = new(i * (gridSize.x + offset), 0, j * (gridSize.y + offset));
                population[i * nPopulation.y + j] = Instantiate(cityPrefab, pos, Quaternion.identity, transform).GetComponent<CityManager>();
                population[i * nPopulation.y + j].cityNumber = i * nPopulation.y + j;
            }
        }
        selectedCity = population[0];
        
        // Connect
        reciever.SinglePortConnect();
    }

    private int selectedCityIndex = 0;

    public void SelectCity(int n){
        selectedCityIndex = n;
        selectedCity = population[n];
    }

    // Update is called once per frame
    void Update() { 
        if (reciever.messagePresent && reciever.serverMsg != null){
            episode ++;
            if(episode > maxEpisodes){
                Reset();
            }
            string[] serverMsgs = reciever.serverMsg.Split(":");
            if(serverMsgs.Length != population.Length){
                Debug.Log("Not enough inputs: " + serverMsgs.Length);
                return;
            } 
            for(int i = 0; i < population.Length; i++){
                population[i].GetStates(serverMsgs[i]);
            }
            mainStateManager.GetStates(serverMsgs[selectedCityIndex]);
            // Send reset message if all cities are full
            if(AllCitiesFull()){
                Reset();
            }
        }
        else{
            Debug.Log("Server message not recieved");
        }
    }

    void Reset(){
        Debug.Log("Resetting.. Episodes Done: " + episode);
        for(int i = 0 ; i < population.Length; i++){
            population[i].Reset();
        }
        episode = 0;
        generation++;
        generationText.text = generation.ToString();
        reciever.reset = true;
    }

    bool AllCitiesFull(){
        for(int i = 0; i < population.Length; i++){
            if (!population[i].cityBuildingPlacer.cityFull){
                return false;
            }
        }

        return true;
    }
}