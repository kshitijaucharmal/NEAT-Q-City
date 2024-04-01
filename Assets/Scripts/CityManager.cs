using UnityEngine;

public class CityManager : MonoBehaviour
{
    public CityInfo cityInfo;
    public BuildingPlacer cityBuildingPlacer;

    void Start(){
        cityBuildingPlacer.Setup();
        cityBuildingPlacer.GenerateBase();
        StartCoroutine(cityBuildingPlacer.PlaceRandom(100));
    }

    void PlaceBuildingBasedOnAction(int b){
        cityBuildingPlacer.BuildBuilding(b);
    }

    void Update(){
    }
}
