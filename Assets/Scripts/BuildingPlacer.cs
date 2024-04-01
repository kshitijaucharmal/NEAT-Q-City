using UnityEngine;
using System.Collections.Generic;
using System.Collections;

public class BuildingPlacer : MonoBehaviour
{
    [SerializeField] private Building[] allBuildings;

    [SerializeField] private Vector2Int size = new Vector2Int(20, 20);
    [SerializeField] private Vector2Int origin;
    [SerializeField] private GameObject basePrefab;

    private Transform city;
    private bool[,] grid;
    private bool basePresent = false;

    public IEnumerator PlaceRandom(int n){
        for(int i = 0; i < n; i++){
            int b = Random.Range(0, allBuildings.Length);
            BuildBuilding(b);
            yield return new WaitForSeconds(0.1f);
        }
    }
    public void Setup()
    {
        InitializeGrid();
        foreach(Building b in allBuildings){
            b.SetHeight();
        }
    }

    public void GenerateBase() {
        city = new GameObject("City").transform;
        city.parent = transform;
        Vector3 pos = transform.position + new Vector3(origin.x + size.x/2, 0, origin.y + size.y/2);
        Transform b = Instantiate(basePrefab, pos, basePrefab.transform.rotation, city).transform;
        b.localScale = new Vector3(size.x, size.y, 1f);
        basePresent = true;
    }

    private void InitializeGrid()
    {
        grid = new bool[size.x, size.y];
        for (int i = 0; i < size.x; i++)
        {
            for (int j = 0; j < size.y; j++)
            {
                grid[i, j] = false;
            }
        }
    }

    private bool IsSpaceAvailable(int x, int y, int width, int height)
    {
        if (x + width > size.y || y + height > size.x)
            return false;

        for (int i = y; i < y + height; i++)
        {
            for (int j = x; j < x + width; j++)
            {
                if (grid[i, j]) return false;
            }
        }
        return true;
    }

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

    private void PlaceBuilding(int buildingIndex, int x, int y)
    {
        Building building = allBuildings[buildingIndex];
        // place a cube of this size at position 
        Vector2Int pos = new(x, y);
        Transform b = CreateBuilding(allBuildings[buildingIndex]);
        b.parent = city;
        var pos3 = new Vector3(pos.x - 0.5f + (0.5f * building.size.x),
                             0.5f * building.height,
                             pos.y - 0.5f + (0.5f * building.size.y));
        b.position = transform.position + pos3;

        for (int i = y; i < y + building.size.y; i++)
        {
            for (int j = x; j < x + building.size.x; j++)
            {
                grid[i, j] = true;
            }
        }
    }

    private Vector2Int GetRandomEmptyPosition(int buildingIndex) {
        Building building = allBuildings[buildingIndex];
        List<Vector2Int> emptyPositions = new List<Vector2Int>();

        for (int y = 0; y <= size.x - building.size.y; y++) {
            for (int x = 0; x <= size.y - building.size.x; x++) {
                if (IsSpaceAvailable(x, y, building.size.x, building.size.y)) {
                    emptyPositions.Add(new Vector2Int(x, y));
                }
            }
        }
        return emptyPositions.Count > 0 ? emptyPositions[Random.Range(0, emptyPositions.Count)] : Vector2Int.zero;
    }

    public void BuildBuilding(int buildingIndex) {
        Vector2Int position = GetRandomEmptyPosition(buildingIndex);
        if (position != Vector2Int.zero)
        {
            PlaceBuilding(buildingIndex, position.x, position.y);
        }
        else
        {
            // 0 is for 1x1 building
            Vector2Int simpleBuildingPosition = GetRandomEmptyPosition(0);
            if (simpleBuildingPosition != Vector2Int.zero)
            {
                PlaceBuilding(0, simpleBuildingPosition.x, simpleBuildingPosition.y);
            }
            else
            {
                Debug.Log("GRID LIMIT EXCEEDED. No space available to place any building.");
            }
        }
    }
}