using System.Text;
using UnityEngine;

public class GridSystem : MonoBehaviour {
  [SerializeField] private Vector2Int gridSize = new Vector2Int(20, 20);
  [SerializeField] private GameObject basePrefab;
  [SerializeField] private Vector2Int origin;

  public Building buildingToPlace;
  public bool basePresent = false;

  private bool[,] grid;
  private Transform city;

  void Start() { }

  // Place building at position
  public void Place() {
    var building = buildingToPlace;
    building.SetHeight();
    Vector2Int pos = FindPositionToPlace(building.size);
    if (pos.x >= 0 && pos.y >= 0) {
      Transform b = CreateBuilding(building);
      // Set parent to city
      b.parent = city;

      // Position the building and place it
      var pos3 = new Vector3(pos.x - 0.5f + (0.5f * building.size.x),
                             0.5f * building.height,
                             pos.y - 0.5f + (0.5f * building.size.y));
      b.position = transform.position + pos3;
      Debug.Log("Created: " + building.name);
    } else {
      Debug.Log("Something in the way");
    }
  }

  // Create a block at buildings position
  public Transform CreateBuilding(Building building) {
    Vector3 dimensions = new(building.size.x, building.height, building.size.y);

    // Create a box based on these dimensions
    var parent = new GameObject(building.name).transform;
    var build = GameObject.CreatePrimitive(PrimitiveType.Cube).transform;
    build.localScale = dimensions;
    build.parent = parent;
    build.GetComponent<Renderer>().material = building.material;
    return parent;
  }

  public Vector2Int FindPositionToPlace(Vector2Int size) { 
    Vector2Int pos = -Vector2Int.one;
    for(int j = 0; j < gridSize.y - size.y; j++){
      for(int i = 0; i < gridSize.x - size.x; i++){
        // Check if occupied
        int x = 0;
        while (x < size.x){
          if (grid[i+x,j]) break;
          else x++;
        }
        // Enough place on x axis
        if(x >= size.x) pos.x = i;
      }
      if(pos.x != -1){
        int y = 0;
        while (y < size.y){
          if(grid[pos.x,j+y]) break;
          else y++;
        }
        if(y >= size.y) pos.y = j;
      }
    }
    if(pos != -Vector2Int.one){
      SetOccupancy(pos, size);
    }else{
      pos -= Vector2Int.one;
    }
    return pos;
  }

  void SetOccupancy(Vector2Int pos, Vector2Int size){
    StringBuilder sb = new StringBuilder();
    for(int i = 0;  i < gridSize.x; i++){
      for(int j = 0; j < gridSize.y; j++){
        if(i >= pos.x && i < pos.x + size.x && j >= pos.y && j < pos.y + size.y){ 
          grid[i,j] = true;
        } 
        sb.Append(grid[i,j] ? "X " : "0 ");
      }
      sb.Append("\n");
    }
  }

  public void GenerateBase() {
    city = new GameObject("City").transform;
    city.parent = transform;
    Vector3 pos = transform.position + new Vector3(origin.x + gridSize.x/2, 0, origin.y + gridSize.y/2);
    Transform b = Instantiate(basePrefab, pos, basePrefab.transform.rotation, city).transform;
    b.localScale = new Vector3(gridSize.x, gridSize.y, 1f);
    basePresent = true;
    // Create Grid
    grid = new bool[gridSize.x,gridSize.y];
    for(int i = 0; i < gridSize.x; i++){
      for(int j = 0; j < gridSize.y; j++){
        grid[i, j] = false;
      }
    }
  }

  public void Clean(){
    while(city.childCount != 0)
    foreach(Transform child in city){
      DestroyImmediate(child.gameObject);
    }

    for(int i = 0; i < gridSize.x; i++){
      for(int j = 0; j < gridSize.y; j++){
        grid[i, j] = false;
      }
    }
    
  }

  void Update(){ }
}