using UnityEngine;

public enum States {
    Population,
    Pollution,
    Recreation,
    Employment,
    Literacy,
    Crime,
    HouseholdIncome,
    GreenSpace,
    Healthcare,
    InternetCoverage,
}

public class StateManager : MonoBehaviour {
    public StatCard population;
    public StatCard pollution;
    public StatCard recreation;
    public StatCard employment;
    public StatCard literacy;
    public StatCard crime;
    public StatCard householdIncome;
    public StatCard greenSpace;
    public StatCard healthCare;
    public StatCard internetCoverage;

    public StatCard GetCard(States state){
        return state switch
        {
            States.Population => population,
            States.Pollution => pollution,
            States.Recreation => recreation,
            States.Employment => employment,
            States.Literacy => literacy,
            States.Crime => crime,
            States.HouseholdIncome => householdIncome,
            States.GreenSpace => greenSpace,
            States.Healthcare => healthCare,
            States.InternetCoverage => internetCoverage,
            _ => population,
        };
    }

    public void Start(){
        for(int i = 0; i < values.Length; i++){
            values[i] = 0.5f;
        }
    }

    float[] values = new float[11];
    public void GetStates(string serverMsg){
        string[] allStates = serverMsg.Split(",");
        for(int i = 0; i < allStates.Length; i++){
            values[i] = float.Parse(allStates[i]);
        }
        // Set Values for values
        population.defaultvalue = values[0];
        pollution.defaultvalue = values[1];
        recreation.defaultvalue = values[2];
        employment.defaultvalue = values[3];
        literacy.defaultvalue = values[4];
        crime.defaultvalue = values[5];
        householdIncome.defaultvalue = values[6];
        greenSpace.defaultvalue = values[7];
        healthCare.defaultvalue = values[8];
        internetCoverage.defaultvalue = values[9];
    }
}
