using System;
using System.Net.Sockets;
using System.Text;
using System.Threading;
using UnityEngine;

public class DataReciever : MonoBehaviour {

  private TcpClient socketConn;
  private Thread clientRcvThread;

  [SerializeField] private StateManager stateManager;
  [Range(0f, 1f)]
  [SerializeField] private float timeBtwnChange = 0.1f;

  [SerializeField] private string host = "localhost";
  [SerializeField] private Vector2Int ports = new(40000, 40016);

  // 10 states
  private string serverMsg;
  private string[] allStates = new string[10];

  private float timeCtr = 0;

  private bool messagePresent = false;
  private bool exit = false;

  void Start() { 
    for(int i = ports.x; i < ports.y; i++){
      try {
        clientRcvThread = new Thread(() => Listen(i));
        clientRcvThread.IsBackground = true;
        clientRcvThread.Start();
      } catch(Exception e){
        Debug.Log("Cannot connect: "+ e);
      }
    }
  }

  void Listen(int port) {
    try {
      socketConn = new TcpClient(host, port);
      Byte[] bytes = new Byte[1024];
      while (clientRcvThread.IsAlive) {
        using (NetworkStream stream = socketConn.GetStream()) {
          int length;
          while ((length = stream.Read(bytes, 0, bytes.Length)) != 0) {
            var incomingData = new byte[length];
            Array.Copy(bytes, 0, incomingData, 0, length);
            serverMsg = Encoding.ASCII.GetString(incomingData);

            // Decode message here
            allStates = serverMsg.Split(",");
            messagePresent = true;

            // Send 'next' after receiving a message
            byte[] nextMessage = Encoding.ASCII.GetBytes("next");
            stream.Write(nextMessage, 0, nextMessage.Length);

            // Send 'exit' to kill
            if(exit){
              byte[] exitMessage = Encoding.ASCII.GetBytes("exit");
              stream.Write(exitMessage, 0, exitMessage.Length);
            }
          }
        }
      }
    } catch (SocketException e) {
      Debug.Log("Socket Exception " + e);
      messagePresent = false;
    }
  }

  // Update is called once per frame
  void Update() {
    if(messagePresent && timeCtr > timeBtwnChange){
      Debug.Log(serverMsg);
      stateManager.GetStates(allStates);
      timeCtr = 0;
    }
    else{
      timeCtr += Time.deltaTime;
      messagePresent = false;
    }
  }

  void OnDestroy(){
    exit = true;
  }
}