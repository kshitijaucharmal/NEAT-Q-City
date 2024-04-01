using UnityEngine;

[System.Serializable]
public class StatCard
{
    public States state;

    [Header("Normal value")]
    [Range(0f, 1f)]
    public float defaultvalue;
}