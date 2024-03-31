using UnityEngine;

[System.Serializable]
public class StatCard
{
    public States state;
    public Texture icon;

    [Header("Normal value")]
    [Range(0f, 1f)]
    public float defaultvalue;
}