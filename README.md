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

**Rest APIs**
- Creating a HELLO WORLD REST API with Python & **Flask**
- Making API Requests using **cURL** and **Postman**
- **CRUD** Operations with Python
- Documenting and Testing REST API with **Swagger**
