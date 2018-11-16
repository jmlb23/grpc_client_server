using Grpc.Core;
using MyGrpc;
using MyServerImplementation;
public class MainRunner
{
    static void Main(string[] args)
    {
        var server = new Server();
        server.Ports.Add(new ServerPort("127.0.0.1",8888,SslServerCredentials.Insecure));
        server.Services.Add(MyService.BindService(new ServiceImplementation()));
        server.Start();
	System.Console.WriteLine("Server Running ...");
	System.Console.ReadLine();
              
    } 
}
