using System.Collections.Generic;

public enum Actions {
    BuildHospital,
    BuildPark,
    BuildFactory,
    BuildRoad,
    BuildEducationInstitute,
    BuildResidentialBuilding,
    BuildOffices,
    BuildPoliceStation,
    BuildTower,
    BuildFarm,
}

[System.Serializable]
public class CityInfo
{
    public Dictionary<States, float> states;
    public Actions currentAction;
}