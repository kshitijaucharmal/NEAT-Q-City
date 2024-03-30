using System.Collections.Generic;

public enum States{
    Healthcare,
    Employment,
    Pollution,
    Literacy,
    Recreation,
    GreenSpace,
    PropertyValue,
}

public enum Actions {
    BuildHospital,
    BuildPark,
}

[System.Serializable]
public class CityInfo
{
    public Dictionary<States, float> states;
    public Actions currentAction;
}