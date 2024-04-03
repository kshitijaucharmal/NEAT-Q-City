using System.Collections.Generic;
using TMPro;
using UnityEngine;

public class CityManager : MonoBehaviour
{
    public BuildingPlacer cityBuildingPlacer;
    public Dictionary<States, float> states;

    public TMP_Text cityNumberText;
    public int cityNumber{
        get{
            return _cityNumber;
        }
        set{
            _cityNumber = value;
            cityNumberText.text = _cityNumber.ToString();
        }
    }

    private int _cityNumber = -1;

    [Tooltip("Should be same order as each city has")]
    public TMP_Text[] buildingCountsUI;

    void Start(){
        cityBuildingPlacer.Setup();
        // StartCoroutine(cityBuildingPlacer.PlaceRandom(100));
        foreach(TMP_Text t in buildingCountsUI){
            t.text = "0";
        }
    }

    public void GetStates(string serverMsg){
        string[] stringForm = serverMsg.Split(",");
        float[] allStates = new float[stringForm.Length];
        for(int i = 0; i < allStates.Length; i++){
            allStates[i] = float.Parse(stringForm[i]);
        }

        // The last element is the action
        int action = (int)allStates[^1];
        TakeAction(action);
    }

    public void TakeAction(int actionIndex=-1){
        if(actionIndex == -1){
            Debug.Log("Action none");
            actionIndex = Random.Range(0, 10);
        }

        // Build the building
        cityBuildingPlacer.BuildBuilding(actionIndex);

        // Set UI Number
        int val = int.Parse(buildingCountsUI[actionIndex].text) + 1;
        buildingCountsUI[actionIndex].text = val.ToString();
    }

    void Update(){
        
    }

}
