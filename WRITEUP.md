# Write-up Template

### Analyze, choose, and justify the appropriate resource option for deploying the app.

*For **both** a VM or App Service solution for the CMS app:*
- *Analyze costs, scalability, availability, and workflow*
- *Choose the appropriate solution (VM or App Service) for deploying the app*
- *Justify your choice*
Reason for Choosing App Service for CMS Deployment:
Analyze Costs

1.App Service: 
Azure App Service offers flexible pricing, ranging from free tiers to paid plans, depending on the resources required. You only pay for what you use, and it’s easy to upgrade or downgrade the service as needed.
Reason for Choosing: I chose App Service because it provides a cost-effective and flexible pricing model that fits within the project budget and allows for easy scaling as demands grow.
Analyze Scalability

2.App Service: 
Azure App Service supports automatic scaling (auto-scaling), enabling the application to handle increased traffic without manual intervention.
Reason for Choosing: The strong scalability of App Service ensures that my application remains stable and responsive, even during sudden spikes in traffic.
Analyze Availability

3.App Service: 
Azure App Service offers high availability with features like geo-redundancy and automatic failover, ensuring that the application remains accessible at all times.
Reason for Choosing: High availability is crucial for ensuring that my application operates continuously, especially for applications requiring constant uptime.
Analyze Workflow

4.App Service: 
Azure App Service integrates seamlessly with DevOps tools like GitHub and Azure DevOps, facilitating automated deployments and minimizing errors during the development process.
Reason for Choosing: The excellent integration with DevOps tools is a significant advantage, making the development and deployment process smoother and more efficient.
Summary: I chose App Service for deploying the CMS application because it offers a flexible, scalable, and highly available solution that integrates well with DevOps tools. These factors ensure that my application runs smoothly and is easy to manage and scale in the future.

### Assess app changes that would change your decision.

*Detail how the app and any other needs would have to change for you to change your decision in the last section.* 

Detail how the app and any other needs would have to change for you to change your decision in the last section.

Changes to the Application Based on My Decision

Change Required: Switching from Azure App Service to an alternative solution like Virtual Machines (VMs) would require me to manage infrastructure configurations, maintenance, and software updates independently. This could increase the complexity of deploying and managing the application and might require additional resources for server configuration and maintenance.
Benefit: Opting for VMs would give me greater control over the infrastructure environment, but it would also mean dealing with more software management and maintenance responsibilities, potentially increasing the risk and management costs.
Other Changes Needed to Suit Application Requirements

Change Requirement: To accommodate the use of VMs, the application would need to be reconfigured to operate within a custom server environment. This includes installing and configuring necessary software, setting up supporting services such as databases and storage, and managing security updates and maintenance.
Implementing Changes: If deciding to switch to VMs, I would need to set up infrastructure management tools and automate deployment processes to minimize errors and optimize performance. This would also require changes in cost and resource management.