# Application-Development-using-Microservices-and-Serverless
https://www.coursera.org/learn/applications-development-microservices-serverless-openshift

**Monolith** vs **SOA**(Service-Oriented Architecture) vs **Microservices**

**Cloud Computing Service Models**
- IaaS (infrastructure as a service): virtualized computing resources over internet -> EC2, etc (the provider manages Networking, storage, physical servers)
- Paas (platform as a Service): a platform to develop, run and manage applications w/o needing infrastructure -> aws elastic beanstalk (the provider manages infrastructure, OS, runtime, middleware)
- SaaS (software as a service): software applications delivered over the internet -> gmail, slack, salesforce (only need your account and usage)
- FaaS (Function as a Service): serverless computing model where you write and deploy individual functions -> aws Lambda, google cloud functions (for event-driven tasks like responding HTTP requests, image processing)

**Microservices Anti-Patterns**
- Don’t build microservices
- Not taking automation seriously
- Don’t build nanoservices
- Don’t turn into SOA
- Don’t build a gateway for each service
  
**Twelve Factor Methodology** (to build **scalable**, **maintainable**, and **portable** applications)
1. Codebase - "One codebase tracked in version control, many deploys."
2. Dependencies - "Explicitly declare and isolate dependencies."
3. Config - "Store config in the environment."
4. Backing Services - "Treat backing services as attached resources."
5. Build, Release, Run - "Strictly separate build, release, and run stages."
6. Processes - "Execute the app as one or more stateless processes."
7. Port Binding - "Export services via port binding."
8. Concurrency - "Scale out via the process model."
9. Disposability - "Maximize robustness with fast startup and graceful shutdown."
10. Dev/Prod Parity - "Keep development, staging, and production as similar as possible."
11. Logs - "Treat logs as event streams."
12. Admin Processes - "Run admin/management tasks as one-off processes."


Swagger UI
![image](https://github.com/user-attachments/assets/7ef88be1-da11-454e-98ad-1e48438a7d72)

postman
![image](https://github.com/user-attachments/assets/0f58a6ca-245f-4dd4-9f1b-cd35b23da9f3)


**Rest APIs**
- Creating a HELLO WORLD REST API with Python & **Flask**
- Making API Requests using **cURL** and **Postman**
- **CRUD** Operations with Python
- Documenting and Testing REST API with **Swagger**
- The **OpenAPI** Specification (OAS) is a standardized format for describing REST APIs.

**GraphQL** (a language-agnostic query language for API, and has one endpoint)
1. Schema: types, queries, mutations, subscriptions.
2. Types: scalars, custom object types, enums, input types.
3. Resolvers: query resolver, mutation resolver, subscription resolver.
4. Queries ![image](https://github.com/user-attachments/assets/50e983ea-a985-4562-b3f7-e37193116920)

5. Mutations ![image](https://github.com/user-attachments/assets/58f97ae3-66b9-433a-a67b-ed96e5beac0f)

6. Subscriptions (allow clients to receive real-time updates) 
7. Execution - GraphQL APIs reply on a runtime to Parse and validate queries against the schema, Delegate query execution to resolvers, Return the results in a predictable format (usually JSON).
8. Tools: GraphiQL/Playground, Apollo Client/Server. Relay.
   ![image](https://github.com/user-attachments/assets/16fbcfcc-f92e-4bb4-9162-cfd7bc1b4090)
   ![image](https://github.com/user-attachments/assets/5a65e3d0-ca86-4d7d-820d-ff1acbd533ad)
   ![image](https://github.com/user-attachments/assets/3b652bcb-eb35-4179-aefa-ce77b2e4a350)
   ![image](https://github.com/user-attachments/assets/85eb7a4c-3496-433f-9d07-740465716371)

GraphQL with Postman:
![image](https://github.com/user-attachments/assets/0029a837-4d93-4a1f-9648-2f0b9d4d7035)
![image](https://github.com/user-attachments/assets/e1d7db75-02ed-4cfa-9bf9-80bdcd8a9cc5)


**Serverless Overview**
![image](https://github.com/user-attachments/assets/e4bf1fae-7a7c-40b3-99f4-460a3386677b)

   
- websocket sessions
- **IBM Cloud Code Engine**:  a fully managed, serverless platform that empowers developers to run containerized applications, batch jobs, and event-driven workloads without needing to manage infrastructure. 
![image](https://github.com/user-attachments/assets/57e72cdc-5684-40ac-8d87-52a734d4fcb5)

Deploying the docker image on Code Engine: <br>
docker build . -t us.icr.io/${SN_ICR_NAMESPACE}/helloworld2 <br>
docker push us.icr.io/${SN_ICR_NAMESPACE}/helloworld2 <br>
ibmcloud ce application create --name helloworld2 --image us.icr.io/${SN_ICR_NAMESPACE}/helloworld2 --registry-secret icr-secret --port 5000 <br>


