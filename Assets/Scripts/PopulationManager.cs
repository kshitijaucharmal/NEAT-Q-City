using UnityEngine;

public class PopulationManager : MonoBehaviour {

    public Vector2Int nPopulation = new(10, 10);
    public Vector2Int gridSize = new(20, 20);
    public int offset = 10;
    public GameObject cityPrefab;

    [HideInInspector]
    public GridSystem[] population;

    // Start is called before the first frame update
    void Start() {
        population = new GridSystem[nPopulation.x * nPopulation.y];
        for(int i = 0; i < nPopulation.x; i++){
            for(int j = 0; j < nPopulation.y; j++){
                Vector3 pos = new(i * (gridSize.x + offset), 0, j * (gridSize.y + offset));
                population[i * nPopulation.y + j] = Instantiate(cityPrefab, pos, Quaternion.identity, transform).GetComponent<GridSystem>();
            }
        }
    }

    // Update is called once per frame
    void Update() {
        foreach(GridSystem gs in population){
            gs.Place();
        }
    }
}