using UnityEngine;

[CreateAssetMenu(menuName = "Simulation/Building", fileName = "Building")]
public class Building : ScriptableObject {
  public new string name;
  public Vector2Int size;
  public int buildingHeight;
  [HideInInspector]public int height;

  public Material material;

  public void SetHeight(){
    if(buildingHeight == -1){
      height = Random.Range(1, 5);
    }
    else{
      height = buildingHeight;
    }
  }
}
