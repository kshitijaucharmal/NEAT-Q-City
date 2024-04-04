using System;
using System.Net.Sockets;
using System.Text;
using System.Threading;
using UnityEngine;

public class DataReciever : MonoBehaviour {

  private TcpClient socketConn;
  private Thread clientRcvThread;

  [SerializeField] private StateManager stateManager;

  [SerializeField] private string host = "localhost";
  //[SerializeField] private Vector2Int ports = new(40000, 40016);
  [SerializeField] private int singlePort = 654321;

  public string serverMsg;
  public bool messagePresent = false;

  private bool exit = false;

  public void SinglePortConnect(){
    try{
      clientRcvThread = new(() => Listen(singlePort, true)) {
          IsBackground = true
      };
      clientRcvThread.Start();
    }
    catch (Exception e){
      Debug.Log("Cannot Connect: " + e);
      messagePresent = false;
    }
  }

  // public void MultiPortConnect(){
  //   popSize = ports.y - ports.x;
  //   serverMsgs = new string[popSize];
  //   messagePresent = new bool[popSize];
  //   for(int i = 0; i < messagePresent.Length; i++){
  //     messagePresent[i] = false;
  //   }
  //   for(int i = ports.x; i < ports.y; i++){
  //     try {
  //       clientRcvThread = new Thread(() => Listen(i));
  //       clientRcvThread.IsBackground = true;
  //       clientRcvThread.Start();
  //     } catch(Exception e){
  //       Debug.Log("Cannot connect: "+ e);
  //     }
  //   }
  // }

  void Listen(int port, bool single = false) {
    bool connected = false;
    try {
      socketConn = new TcpClient(host, port);
      connected = true;
    }
    catch(SocketException e){
      if (e.SocketErrorCode == SocketError.ConnectionRefused) {
        Debug.Log("Connection refused on port " + port);
        // Wait for some time before retrying
      } else {
        Debug.Log("Socket Exception " + e);
        return; // Exit method if it's a different socket exception
      }
    }
    
    if(!connected) return;
    try{
      Byte[] bytes = new Byte[1024];
      while (clientRcvThread.IsAlive) {
        using (NetworkStream stream = socketConn.GetStream()) {
          int length;
          while ((length = stream.Read(bytes, 0, bytes.Length)) != 0) {
            var incomingData = new byte[length];
            Array.Copy(bytes, 0, incomingData, 0, length);
            if(single){
              serverMsg = Encoding.ASCII.GetString(incomingData);
              messagePresent = true;
            }
            else{
              // serverMsgs[port - ports.x] = Encoding.ASCII.GetString(incomingData);
              // messagePresent[port - ports.x] = true;
            }

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
      // messagePresent[port - ports.x] = false;
      messagePresent = false;
    }
  }

  void Update(){
  }

  void OnDestroy(){
    exit = true;
  }
}