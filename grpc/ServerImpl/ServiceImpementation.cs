using System;
using System.Threading.Tasks;
using System.Collections.Generic;
using MyGrpc;

namespace MyServerImplementation
{
class ServiceImplementation : MyService.MyServiceBase
{
    Dictionary<int,Person> mockRepo = new Dictionary<int, Person>()
    {
        {1, new Person(){ Name = "Jesus", Surname="Lopez"}},
        {2, new Person(){ Name = "Antonio", Surname="Lopez"}},
        {3, new Person(){ Name = "Pepe", Surname="Lopez"}},
    };
    public override Task<NameAndSurname> Search(Request request, Grpc.Core.ServerCallContext context)
    {
        var entry = mockRepo[request.Id];
        
        var response = new NameAndSurname(){ Name = entry.Name, Surname = entry.Surname };

        return Task.FromResult(response);
    }
}

class Person
{
    public string Name { get; set;}
    public string Surname { get; set; }
}
}
