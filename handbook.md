# Appian Handbook

Auto-updated from public Appian release notes. Shows the most recent 2 releases. Not affiliated with or endorsed by Appian Corporation.


---

## Appian 26.6 — synced 2026-08-16

Source: https://docs.appian.com/suite/help/26.6/Appian_Release_Notes.html

# Appian Release Notes

26.6 Product Webinar

Join our Appian marketing team and other Appian experts as they dig into highlights from the 26.6 release. You can also checkout our Release Showcase course on Academy Online to take a deeper dive into the latest features.

Join our Appian marketing team and other Appian experts as they dig into highlights from the 26.6 release. You can also checkout our Release Showcase course on Academy Online to take a deeper dive into the latest features.

Access new features and improvements every month on Appian Cloud

## Release Highlights

### Connect AI agents to external tools instantly with MCP

Version : 26.6

Expand the capabilities of your AI agents by connecting them directly to external enterprise systems using Model Context Protocol (MCP). Instead of building complex custom integrations for every third-party platform, you can now use a generic MCP connected system to link your AI agents to tools like GitHub, Snowflake, and Google Drive. This streamlined integration allows you to incorporate external capabilities into your AI agent's toolkit, eliminating development overhead and dramatically reducing your maintenance burden.

### Use natural language to plan and build applications

Turn your requirements into working applications with Appian Composer and its new capability, dev agent —an intelligent assistant for end-to-end application development. This connected experience helps you organize development, delegate work to AI, and stay in control of every change.

You can choose how much AI assistance to use as you build. Have Composer generate the foundational design objects for your application, or build manually and use the dev agent when you want AI support.

When you start building from Plan view, your stories become trackable development work on a kanban-style board , giving you a clear view of progress and the tasks that remain. When you're ready, simply assign specific tasks to the dev agent for automatic execution.

Dev agent isn't limited to story tasks, either–—you can use plain language anytime to build brand-new design objects or edit existing ones on the fly. Instead of updating each record type, interface, process model, and expression rule individually, use specific and natural language to describe your overall goal for the business objects and application. Whether you're working from the Board tab , the Build view , or an interface object , the dev agent coordinates the necessary updates and accounts for dependencies between objects. Step-by-step previews and real-time feedback let you review each change, giving you the speed of AI-assisted development without losing oversight.

### Appian and Snowflake partner to activate data & AI in process

Version : 26.6

We've added native support for Snowflake—allowing you to put advanced data and AI intelligence to work within mission-critical business applications.

To get started, create a Snowflake connected system to access data from anywhere in Snowflake. From there, you can quickly build a record type that connects directly to your entire history of enterprise data in Snowflake. This unlocks instant access to your largest datasets alongside powerful features like relationships, record-level security, and custom record fields—all without syncing your data.

You can also equip your Appian AI agents with advanced Snowflake Cortex AI and ML capabilities through MCP. Snowflake Cortex AI enables custom model training for fraud and anomaly detection and much more, allowing you to more easily leverage industry-leading AI directly within Appian.

### Introducing releases: A new way to manage deployments

Version : 26.6

Introducing " releases ," a new out-of-the-box way to manage and organize large deployments for your most interconnected apps. Releases allow you to group multiple packages of related functionality and easily deploy multiple packages from multiple apps at one time!

With releases, you can start organizing for deployment while you plan your team's development timeline. Once you've created your release, you can add it to your packages as you go! Then, when you're ready to deploy, breathe easy knowing all your team's work is already ready to go.

Since releases have built in alerts to ensure that objects across releases don't overlap, using releases throughout development helps ensure your team is up-to-date with conflicting changes in your environment. These alerts help you avoid deploying features before they're ready by automatically highlighting when objects in packages are shared between multiple active releases.

And, releases even help you stay organized after you deploy! Just deploy your packages, and we'll automatically group up the relevant objects into a new generated package for the release in your target environment. This helps you easily keep all your objects together in intermediate testing environments and make deploying to production environments a breeze.

Releases are the ideal way to easily manage your development and deployment lifecycle. From sprint planning to deployment and beyond, releases provide you with native tooling for planning, tracking, and ultimately deploying your functionality, streamlining every step of your feature lifecycle.

### Deploy multiple packages from multiple apps in a single action

Version : 26.6

We're excited to announce that we're significantly streamlining deployments with the ability to deploy multiple packages from multiple app s in one deployment. Whether you're deploying manually, externally, or directly across environments, you can now select and deploy multiple packages from multiple apps in just a few clicks!

And, you'll notice that Compare and Deploy has a sleek new look and feel, perfect for moving quickly and efficiently through your deployment process.

You can also start direct and manual deployments right from the Packages view, both for an individual app and the entire environment!

This new powerful approach to deployments not only speeds up the time to delivery, but also reduces effort, increases deployment flexibility and consistency, and helps you more confidently move from development to production.

## Deployments

### A new centralized view for packages

Version : 26.4

Experience a more unified way to work with the new Packages view in Appian Designer. Here, you can view and manage packages across your entire environment or within a single application.

Package view filters help you quickly find packages by name, application, releases, or even the objects within them. And, you can efficiently manage packages with bulk actions like associating multiple packages with a release or deploying multiple packages from the same app at once.

By unifying and simplifying package management in a single, intuitive view, we're helping you to stay organized and efficient from development to deployment.

### More comprehensive releases with package limit increase

Version : 26.5

You can now have up to 500 packages per app! By upping the limit from 100 to 500, your teams have more room to organize a full deployment cycle without running out of capacity. And, the higher limit means less frequent manual cleanup.

## AI Agents

### Accelerate AI agent prototyping with a unified build experience

Version : 26.6

Build, test, and refine your AI agents without ever losing your context. The enhanced Build tab for AI agents unifies configuration and testing into a sleek split-pane layout, saving you from switching tabs while you prototype. Keep your core instructions visible while managing tools, and reuse your saved test cases instantly from a new dropdown.

We've also made test results more readable by automatically formatting the text. Your tables, lists, and code blocks now show up beautifully in real time so you can review your work at a glance.

Speed up your design iterations and deploy production-ready AI agents faster than ever!

### Streamline AI agent evaluation

Version : 26.6

Deploy your AI agents with absolute confidence using a systematic quality workflow. The new Evaluate tab in the AI agent object provides a centralized space to manage your test cases and run them in bulk. Instantly verify performance across critical scenarios, catch regressions early, and review side-by-side results—no need to supervise individual runs.

We've also introduced inline feedback. Now, you can record clear thumbs-up or thumbs-down ratings directly on evaluation results. These insights automatically aggregate into powerful metrics like overall accuracy, right on the Evaluate tab.

With this centralized view of your test results, you'll immediately know when your AI agent is ready for production.

### Accelerate AI automation with parallel tool execution

Version : 26.6

Accelerate your AI-driven business processes and cut operational costs with concurrent tool execution. Your AI agents now run multiple independent tool calls simultaneously instead of waiting through sequential, step-by-step workflows. This streamlined approach eliminates wait times and reduces AI action costs, getting your high-volume automations to the finish line faster.

### Engage users with chat agents

Version : 26.6

Create dynamic, conversational experiences for your users right inside your application layouts. With the new a!agentChatField component , you can confidently deploy dedicated Appian AI agents that communicate directly with your users through a chat interface. This makes it simple to embed real-time AI guidance directly into your daily workflows, transforming how your users interact with your applications.

## Scale your enterprise AI strategy with the Appian MCP Server

Version : 26.6

Extend your enterprise AI strategy by linking Appian application data and workflows directly to third-party agent platforms. The new Appian Model Context Protocol (MCP) Server allows you to connect record types, process models, and expression rules as secure, discoverable tools for external agents. This centralized foundation ensures external assistants safely leverage Appian's robust security and underlying process logic without requiring custom connections or redevelopment.

## AI governance

### Connect your Microsoft Azure OpenAI accounts to Appian

Version : 26.6

Maintain complete control over your generative AI traffic by connecting Appian directly to your organization's Microsoft Azure OpenAI accounts. This connection allows you to use your trusted Azure infrastructure to power features like AI Skills and the a!genAiModels() function, ensuring your data stays within the security boundaries you've already established.

### Fuel your AI-powered features with Amazon Nova 2 Lite

Version : 26.6

Appian AI skills and other AI-powered features now support Amazon Nova 2 Lite , expanding your options for powering AI experiences in Appian. With text and vision capabilities, Nova 2 Lite offers a fast, reliable alternative to Anthropic models and helps organizations meet regional availability and compliance requirements while taking advantage of Appian AI.

### Centralize AI security with environment-wide guardrails

Version : 26.6

Secure every generative AI interaction across your entire environment with centralized AI guardrails that automatically protect your data and users. Managed directly from the new AI Guardrails tab of the Admin Console, these protections evaluate all inputs and outputs for risks like prompt injection, toxic content, and PII leakage. Centralizing your security across all AI models and providers in your environment ensures uniform protection for your apps, so your developers can focus on building high-impact AI features at scale.

### Secure your AI supply chain with model family controls

Version : 26.5

Maintain strict compliance and secure your AI processes with new environment-level controls for model providers. You can now disable specific model families to meet regulatory mandates while keeping your Appian AI features fully operational through alternative providers. This targeted control ensures you never have to choose between meeting security requirements and leveraging the power of Appian AI.

### Expanded regional support in Japan: Osaka

Version : 26.4

We are excited to expand Appian AI regional support in Japan with the addition of the Osaka region. This expansion enables localized, in-country disaster recovery, allowing you to meet strict regulatory mandates for geographic separation while minimizing potential downtime—all within your required data residency boundaries.

### Power Appian AI with your LLM gateway

Version : 26.4

Now, even organizations with the strictest governance requirements can harness the power of generative AI in Appian applications while maintaining absolute centralized control over security, auditing, and costs.

Administrators can configure and register a custom AI provider endpoint in the Administration Console , allowing Appian to connect seamlessly with internal gateways and proxy services. This guarantees that every single AI request is routed through your approved, internal platforms.

### Build future-proof AI applications with dynamic model metadata

Version : 26.6

Build applications that automatically adapt to evolving AI model requirements without constant manual updates. The a!genAiModels() function now dynamically returns up-to-date model specifications—including file sizes, page limits, and spreadsheet constraints. By dynamically returning this metadata, your applications seamlessly scale alongside new models and backend improvements without requiring code modifications or separate deployments.

## AI skills

### Monitor and track AI Action consumption at the execution level

Version : 26.6

Track and govern your generative AI costs with complete execution-level visibility. The Execute Generative AI Skill , Advanced IDP Tools , and Extract from Document smart services now include an AI Actions Consumed output instead of separate input and output token metrics. This field directly mirrors your platform's billing model, giving you immediate transparency into exactly how many AI actions each execution consumes.

Further, use the optional Usage Groups input on the Execute Generative AI Skill smart service to map AI Action consumption directly to specific Appian groups, enabling precise cost attribution across departments.

The AI Skill test panel also displays AI Actions Consumed , so you can monitor consumption during development.

### Process text and Word documents natively in AI skills

Version : 26.6

Accelerate your document workflows by passing common business files directly to your generative AI skills . We've expanded native file input capabilities to support TXT, Markdown, HTML, and DOCX formats—eliminating the overhead of building and maintaining manual conversion pipelines. Processing these files in their original formats prevents formatting loss and dropped images, ensuring your AI skills deliver maximum extraction and classification accuracy.

### Process dense documents faster with Claude Sonnet 4.6

Version : 26.6

Bring the power of Claude Sonnet 4.6 to your generative AI skills. This latest Anthropic model is built on AWS Bedrock and offers a larger context window with no additional cost, allowing you to seamlessly process text-heavy documents in a single pass. Upgrade your AI skills today to supercharge your document automation and keep your applications on the cutting edge.

### Process longer documents with expanded PDF support

Version : 26.5

Take your document automation to the next level with native PDF support for our most advanced AI models. You can now process files up to 100 pages when using visual elements and text mode, a major increase from the previous 20-page limit. This enhancement can even provide improved results when reading handwriting and checkboxes, so you can automate your most data-heavy workflows with more speed and accuracy than ever.

### Extract data with the Spreadsheet Extraction AI skill

Version : 26.4

Automate your spreadsheet data extraction more accurately than ever with the new Spreadsheet Extraction AI skill . You can now process Microsoft Excel files natively—no manual conversions required—saving you time and reducing errors. This AI skill precisely identifies data across complex, multi-sheet reports to deliver the exact values you need.

DocCenter 4.2 includes built-in Excel extraction and reconciliation capabilities using this AI skill. Building on the platform capabilities, DocCenter can extract data from spreadsheets spanning multiple sheets and thousands of cells, preserving the original file's structure for simpler cross-referencing during reconciliation.

## Appian Composer

### Start application planning by previewing and editing your app's user experience

Version : 26.6

Appian Composer now has a redesigned visual workspace that lets you interact with a clickable preview of your application immediately after the planning phase. Generated screens are dynamically tailored based on your specific requirements, so you only get the screens your application actually needs.

This whiteboard-style experience allows you to navigate through the entire application flow from dashboards to forms, before even a single design object is created. If you want to adjust what you see, Composer can help you refine layouts, update navigation links, and adapt screens in real time to match your exact vision.

### A more connected Composer

Version : 26.6

Plan your applications with more continuity and speed using the updated chat in Composer . Your conversations now persist across every tab in the Plan view, eliminating the need to repeat context as you transition between tabs.

We've also polished the chat interface and formatting to make your interactions seamless and accessible. This streamlined experience provides an intuitive way to interact with your application plan and helps you keep your focus where it belongs—building great applications.

### Upload rich files to ground your app in real requirements

Version : 26.6

Bring your existing assets directly into Composer to keep your plans grounded in your source material. You can now upload XML, YAML, and PPTX files , and up to 20 images, such as BPMN diagrams and screenshots of legacy UIs—all alongside your requirements. Every file you upload is automatically stored in Application Documentation, giving you built-in requirements traceability from day one.

### Modernize your spreadsheets into full app plans automatically

Version : 26.6

Building on its ability to import Excel files , Appian Composer now automatically interprets the formulas, conditional logic, and macros within your Excel-based EUCs to extract business requirements. This helps you easily generate a modernization plan that accurately mirrors your legacy app's functionality—saving you from all that manual conversion.

## RPA

### Automate complex web workflows with native browser actions

Version : 26.6

Build secure, compliant web automations without relying on community plugins. Appian RPA now includes native support for closing active tabs and improved table value extraction in robotic tasks.

The enhanced Get Table Value action now allows robots to extract values from more non-standard web tables, like tables where there are fewer header cells than data cells. This update lets you leave fragile workarounds in the past, while improving the stability and reliability of your web automation workflows.

### High availability for Appian RPA

Version : 26.4

Keep your most important RPA automations running smoothly with high availability (HA) for Appian RPA. This enhancement ensures your robotic tasks remain resilient and scalable, even during periods of high demand. By protecting your business from unplanned downtime, you can confidently scale your operations and ensure your critical processes are always available.

High availability for RPA is available upon request. Contact Appian Support to enable this feature for your environment.

To optimize your automation resilience, see High Availability for RPA .

### Automate RPA infrastructure at scale

Version : 26.4

Appian RPA introduces secure REST APIs to automate the management of credentials and Virtual Desktop Infrastructure (VDI) configurations. You can now programmatically rotate passwords and update autologin credentials instead of performing manual tasks in the RPA Console. These new endpoints eliminate maintenance bottlenecks and allow you to manage large-scale robot deployments with secure, automated workflows.

### RPA Queues and Schedules removed

Version : 26.5

RPA Queues and Scheduling, deprecated in RPA 9.17, are now fully removed in RPA 9.22. If you haven't already, migrate your schedules to Appian process model Timer Events and replace queues with LCP patterns.

### Reserve a specific credential by UUID

Version : 26.5

The Reserve Credential action now supports credential UUIDs as fixed inputs or expressions. This lets you configure automated workflows to use a specific stored credential instead of selecting one from a credential pool. With more precise control over credential selection, you can support automation patterns such as password rotation without manual intervention.

### Manage support files faster in high availability environments

Version : 26.5

Using support files in HA deployments is now faster than before. We optimized how support files are managed in HA architectures, so actions like uploading, downloading, renaming, moving, and extracting now complete in seconds.

### Improved stability for high-volume executions

Version : 26.5

We enhanced how the RPA server handles concurrent robot authentication to better protect performance as volume increases. These improvements keep execution queuing stable even when multiple robots connect at the same time.

## Data fabric

### Extend your data fabric to external AI agents

Version : 26.6

Appian's data fabric is the backbone of your applications, Process HQ, and Appian AI agents. Now, you can securely extend that same reliable foundation to third-party agentic AI providers using the Appian MCP Server .

Through the new Query Data Fabric tool, external AI agents gain structured access to your data for metadata discovery and SQL-based retrieval. The MCP server can discover all synced record types, but Appian automatically enforces your established object, field, and row-level security so external agents only access the data they're authorized to use.

### Supercharge your data fabric with autoscale

Version : 26.6

Autoscale for data fabric dynamically scales your data service up and down to match query demand—no manual sizing, no maintenance. Appian manages everything for you so your record type queries stay fast no matter how much activity spikes.

When using autoscale for data fabric, the data service moves off your environment onto compute-optimized Appian Cloud infrastructure. This frees up resources and accelerates query performance for compute-intensive query workloads by up to 2x. Open a support case to enable autoscale for data fabric and let Appian handle the heavy lifting.

### Instantly understand your data with the record type Overview page

Version : 26.4

Introducing the new record type Overview page. This page provides a centralized view for all your data details—including the data source, row count, sync status, and object-level security. To give you instant clarity on the purpose of the record type, we've added an AI-generated summary that describes its role and purpose in your application.

You can also quickly show your record type as a dataset in Process HQ , enabling you and your business users to jump straight into high-level reporting and analysis. This streamlined view helps you stay organized and build faster with a complete understanding of your data.

### Unlock the full power of your external documents

Version : 26.4

We're expanding the reach of your data fabric so you can integrate even more external documents into your applications. Now, you can use record types to access documents from connected system plug-ins , giving you the flexibility to unify your enterprise documents regardless of where they're stored.

To help you navigate your data faster, you can also use smart search to find information within these external files. Combined, these enhancements allow you to seamlessly access all documents in the record type and ensure that you and your users can find exactly what you need in an instant.

### Securely connect to more databases without syncing

Version : 26.5

We're continuing to expand Appian's data fabric by adding PostgreSQL to our list of supported data sources for unsynced record types . This means you can now build record types that connect directly to your PostgreSQL databases and leverage powerful features like record-level security and relationships.

To make these external connections even more secure, you can now use direct data access to connect to your databases via VPN or PrivateLink . This gives you the flexibility to meet strict infrastructure requirements while building data-rich applications fast.

### Search across larger documents

Version : 26.4

Smart search can now handle PDF and DOCX files up to 200MB! By increasing these document size limits, you can now index and search some of your largest files.

### Build more precise queries with smart search

Version : 26.6

You can now combine both smart search operators within a single a!queryRecordType() expression to perform a semantic search and a lexical search on the same field. By leveraging the strengths of both search methods at once, you can dramatically increase search accuracy and help your users find the right information faster.

We've also expanded AI-powered smart search capabilities to the a!relatedRecordData() function , allowing you to use semantic or lexical search to find related data. For example, you can query customers and their related support cases that are semantically similar to "outages"—uncovering a more comprehensive list of cases, like those about "network problems" or "connection failures", without needing an exact keyword match.

### Sync multiple record types at once

Version : 26.5

You can now sync multiple record types at the same time from the Monitor view . In just a few clicks, you can start full syncs to ensure your record data is fully up to date with the source and ready to go.

### Sync high-volume data with more flexibility

Version : 26.4

You can now leverage the Keep data available at high volumes setting with both incremental and smart service syncs . This added flexibility ensures your record types remain available at scale, regardless of how you choose to sync your data. If a sync ever exceeds your row limit, we'll automatically handle the overflow so your record types always have the latest information. It's never been easier to keep your most important data up to date and ready for action.

### Analyze record view and action performance directly from your record types

Version : 26.4

We've made it easier to optimize your record views and actions by bringing query performance data directly into the record type's Performance page .

Now, you can instantly see how much data your record view or record action components are querying. This allows you to identify if those queries are slowing down your interfaces or requesting unnecessary fields—helping you build faster and more efficient interfaces and processes.

## Integrations

### Connect your business processes to real-time Kafka events

Version : 26.6

Bring the power of event-driven architecture into your Appian applications with our Apache Kafka integration , the supporting event consumer object, and the Publish Event smart service.

Start by setting up your connection once with an Apache Kafka connected system . When the connected system is set up, create and configure a new event consumer object to link your Kafka topic to Appian.

With the event consumer , you can listen to a Kafka topic, filter incoming events using expressions, and automatically write records or trigger a process model for each matching event.

With the Publish Event smart service , you can set up your process models to push vital data so other systems can take action on that information. To get started, add the new smart service, fill in the details of your Kafka broker, and specify the info you want to publish. Once the smart service is configured, Appian will start publishing events to the broker automatically.

Whether you're processing new orders, flagging fraud, or onboarding employees, you can now connect your existing process models to activity happening across your enterprise—all without leaving Appian.

### Securely connect to Kafka brokers with OAuth and SCRAM

Version : 26.5

The Apache Kafka connected system now supports OAuth client credentials and Salted Challenge Response Authentication Mechanism (SCRAM) authentication for both SASL and SASL_SSL protocols. These capabilities ensure organizations can effortlessly meet rigorous Information Security (InfoSec) compliance standards without compromising ease of connectivity.

### Secure your PostgreSQL connections with OAuth 2.0

Version : 26.6

You can now use the OAuth 2.0 Client Credentials Grant to authenticate your PostgreSQL databases, whether you're using standard OAuth 2.0 or Azure AD. This new option provides another robust and effective layer of security for both synced and unsynced record types.

### Granular scope control for HTTP connected systems

Version : 26.4

We're giving you more flexible OAuth 2.0 configurations for your HTTP connected systems . While most identity providers allow scopes in the request, those strictly following RFC 6749 require that the scope parameter is omitted during the backend token exchange. With one checkbox, you can now choose whether to include scopes during these token exchanges to meet different levels of OAuth spec compliance.

To ensure compatibility with your existing connected systems, this option is enabled by default. This keeps your integrations robust and reliable, no matter the requirements of your external data sources.

### Pre-configure your PrivateLink connections for Enhanced Business Continuity

Version : 26.5

You can now work with Appian Support to configure AWS PrivateLink connections in your secondary Appian Cloud region ahead of time.

For Outbound PrivateLink , Appian can now host VPC Interface Endpoints in your primary and secondary regions using the same hostname. During a regional failover, your site will automatically switch to the backup PrivateLink. Failover is seamless—you no longer need to update your integrations to point to a separate hostname after starting your site. Ensure that you maintain VPC Endpoint Services in your primary and secondary regions.

For Inbound Privatelink , Appian can now host VPC Endpoint Services in your primary and secondary regions. You will need to provision VPC Interface Endpoints in your primary and secondary regions. Ensure your routing failover mechanisms are able to seamlessly transition to your backup Interface Endpoints.

To pre-configure your PrivateLinks for Enhanced Business Continuity, contact Appian Support . This functionality is supported for PrivateLink connections on any version of Appian Cloud.

## Process modeling and autoscale

### More synchronous actions in autoscaled processes with activity chaining

Version : 26.4

In 26.3, we unlocked attended autoscaled processes with process start forms . Now, we're excited to open up more attended use cases with support for activity chaining.

When users launch a record action or start process link , they'll complete the configured start form and wait for any chained activities to complete. This provides a more intuitive workflow for your users and lets you improve their experience working with data in your applications.

### Scale up process execution with multiple node instances (MNI)

Version : 26.5

Autoscaled processes can now run multiple instances of a node, letting you work through large sets of tasks without needing to build and test complex loops. You can set up MNI in the node properties with only a few clicks—just like in standard processes!

### Use more smart services in autoscaled processes

Version : 26.5

It's now easier than ever to migrate your existing process models to use autoscale. In 26.5, we've expanded support by adding smart services for AI skills, RPA, and identity management:

- Add Group Admins Smart Service

- Add Group Members Smart Service

- Change User Type Smart Service

- Classify Documents Smart Service

- Classify Emails Smart Service

- Create Group Smart Service

- Create User Smart Service

- Deactivate User Smart Service

- Delete Group Smart Service

- Edit Group Smart Service

- Execute Robotic Task Smart Service

- Extract from Document Smart Service

- Modify User Security Smart Service

- Reactivate User Smart Service

- Reconcile Doc Extraction Smart Service

- Remove Group Admins Smart Service

- Remove Group Members Smart Service

- Rename Users Smart Service

- Set Group Attributes Smart Service

- Update User Profile Smart Service

In 26.4, we expanded support by adding smart services for constants and document management:

- Create Knowledge Center Smart Service

- Delete Folder Smart Service

- Delete KC Smart Service

- Edit Document Properties Smart Service

- Edit KC Properties Smart Service

- Export Data Store Entity to CSV Smart Service

- Export Data Store Entity to Excel Smart Service

- HTML Doc From Template Smart Service

- Increment Constant Smart Service

- Lock Document Smart Service

- Modify Folder Security Smart Service

- Modify KC Security Smart Service

- Move Document Smart Service

- Move Folder Smart Service

- MS Word 2007 Doc from Template Smart Service

- Open Office Writer Doc From Template Smart Service

- PDF Doc From Template Smart Service

- Rename Folder Smart Service

- Text Doc From Template Smart Service

- Unlock Document Smart Service

- Update Constant Smart Service

### Timer-based exception flows in autoscaled processes

Version : 26.5

In 26.4, we enabled rule event exceptions in autoscale and we are continuing to expand this functionality with timer-based exceptions . You can now configure nodes to automatically take an exception flow after an interval you define. With this latest update, we're giving you more flexibility in your process design so that you can keep your users on track and on time.

### Rule events and exception flows in autoscaled processes

Version : 26.4

More sophisticated process flows are now possible with rule events and rule event exceptions in autoscale. You can now configure nodes to evaluate business rules at the start of execution, automatically skipping tasks to ensure your automation always follows the correct path. This update streamlines how you handle complex scenarios, ensuring you deliver a seamless experience for every user.

### Support for Enhanced Business Continuity with autoscaled processes

Version : 26.4

If you use Enhanced Business Continuity for Appian Cloud, you can now recover autoscaled process data in the event of a region-wide failure. This change ensures critical business process data is available within your recovery point objective (RPO) window.

### Use smart service plug-ins in autoscaled processes

Version : 26.6

Autoscaled processes now support Appian-authored smart service plug-ins out of the box. These tools let you take advantage of extended functionality in autoscaled process models to better meet your use cases. Use the AppMarket to find plug-ins that can be used right away—no additional setup required!

If you need to use other smart service plug-ins in your autoscaled processes, contact Appian Support.

### PrivateLink support for autoscaled processes

Version : 26.6

PrivateLink can now be used with autoscaled processes, giving you more options for keeping your data secure and conforming with your unique security requirements.

## Process HQ

### Uncover real-world process insights in self-managed environments

Version : 26.6

This release, we're bringing the powerful ability to analyze process data directly to Appian on Kubernetes . You can now run our advanced process analysis tools entirely inside your own infrastructure, completing your Process HQ workspace. With process insights in your self-managed environment , you can confidently eliminate operational bottlenecks while ensuring data sensitivity and complying with locality requirements.

### Build reports with process data

Version : 26.6

Process HQ's custom reports empower business users to independently explore and analyze your enterprise data. Now you can use this same flexible, intuitive report creation tool to build reports on your process data using the results of your process analysis .

We've added processes to the data catalog , so you can easily review your processes alongside your datasets, and quickly start building reports from your data. This powerful new capability allows users to compare metrics, like average time spent across tasks types, in a single chart. Users can design, filter, share, and add these reports to dashboards just like any other report in Process HQ.

And, to provide a unified development experience, we've added process reports as a supported report type in the report object . This allows you to configure report properties and deploy your process reports with your apps and packages.

With this update, we're giving you more power to uncover valuable, actionable insights into your business data.

### Discover suggested insights for count KPIs

Version : 26.5

Count KPIs measure critical process inefficiencies like stale cases, incidents, and other exceptions to your organization's typical workflow. With this release, we're helping you uncover the root cause of these issues more easily than ever with suggested insights.

Process HQ can now automatically generate suggested insights for your count KPIs, just like the existing insights for duration KPIs. Now, when you drill down to insights in your process, you can review the suggested insights, save them with a single click, and use them as a starting point for even deeper analysis.

### Uncover suggested insights with the interactive process diagram

Version : 26.6

We're making it even easier to explore your process data and discover suggested insights , accelerating your time to real process improvements. Now, you can click on any activity or sequence in the process diagram to open more details and easily create a focused KPI with suggested insights. If the KPI is helpful, you can save it, or keep exploring the process diagram.

With this update, you can create KPIs and discover insights faster than ever before.

### Easily discover and manage your datasets from Process HQ

Version : 26.4

Preparing your data for Process HQ is now more intuitive and efficient. The Data Governance page features a new semantic search, allowing you to find relevant record types without knowing the exact name.

Once you've found your record type, you can review an AI-generated summary and choose whether to show the record type and its related record types as datasets . These enhancements give you the speed and control needed to quickly transform your information into actionable business insights.

### Instantly view existing reports and dashboards for your datasets

Version : 26.4

The Data Catalog now gives you a more complete picture of how your organization uses its data. When you select a dataset, you'll instantly see all the reports and dashboards already built from it, as well as the specific data that makes up the dataset. This added visibility helps you avoid duplicating effort and ensures you have the context you need before you start building reports.

### Set target performance for KPIs

Version : 26.4

We've added configurable targets for duration KPIs , so you can quickly see how well the KPI is performing compared to your expectations or goals. Use a target to easily measure the KPI's conformance to a standard value, or track progress towards a specific process improvement.

When you configure a target, we'll generate suggested insights to help you improve your processes and achieve your target performance.

### Create and deploy business processes

Version : 26.4

We're continuing to improve the unified development experience for Process HQ with the new business process design object .

Now, instead of adding processes in production in Process HQ, developers can create business process objects during development in Appian Designer. This allows you to create Process HQ processes and deploy them just like any other design object, so processes are instantly available in Process HQ as soon as you deploy your app.

### Design richer dashboards with adjustable layouts

Version : 26.5

Process HQ's easy-to-use dashboard builder just got even more powerful. You can now customize your dashboards exactly how you want! It's easy to adjust the height and width of reports and process KPIs when you drag and drop them onto a dashboard. And, you're even able to make items span multiple rows. Finer control over your dashboard layout is just a few clicks away.

### Duplicate dashboards to build more quickly

Version : 26.6

We've added the ability to duplicate entire dashboards , so you can easily create new ones without having to start from scratch. The new dashboard will have all the same items and layout as the original, and you can even copy the security settings for easy sharing.

### Visualize automation performance and opportunities in your process

Version : 26.5

This release, we're displaying more details about exactly who is performing each step of your process directly on the process diagram . Activity nodes now feature intuitive icons that show who or what is responsible for completing steps in your process—whether it's a human, RPA bot, AI agent, or integration—eliminating the need to cross-reference multiple sources. Simply hover over an icon to see a full breakdown of automation types for that activity.

This enhancement highlights critical insights into your hybrid workflows, helping you monitor AI performance and identify new automation opportunities with ease.

### Expand your processes with more unique activities

Version : 26.5

We've expanded the limit for unique activities in a process from 50 to 100 to help you model the complex, high-density workflows that drive your enterprise.

### Customize your chart scale with axis settings

Version : 26.4

Report creators can now customize chart axes in reports to better highlight variance between data points, especially when comparing high-volume values. By adjusting the chart axis, you can make subtle trends and performance gaps visible at a glance.

### Manage reports with the new action menu

Version : 26.4

We've added a new actions menu to reports pages, so common tasks are just a click away. Now you can view and edit report properties , duplicate a report , and add a report to an app , all without leaving the report page.

We've also updated the report properties to show the report's dataset, so users can easily identify the source of the report's data.

## Appian Designer

### Build applications faster with a streamlined design object menu

Version : 26.4

We've tidied up the design object menu to help create a faster development experience. This streamlined menu lets you quickly browse all available design objects and stay focused on building your application.

## Sites and portals

### Apply unique typefaces to individual sites and portals

Version : 26.5

Deliver a more tailored user experience by applying custom typefaces to specific sites and portals. Using CSS profiles , you can now independently select fonts for each site or portal, ensuring every page aligns with your specific brand guidelines. This granular control allows you to effortlessly manage diverse requirements across multiple brands or business units, all within a single Appian environment.

### Expand your branding flexibility with new CSS profile properties

Version : 26.6

We're continuing to deliver more robust CSS profiles capabilities with the introduction of even more properties . In 26.4, we released properties to give you more control over the look of radio buttons, checkboxes, and card and box shadows, as well as to change the base font size across sites and portals.

In 26.6, we're introducing properties that allow you to customize background colors for inputs and pop-up menus, such as those in text inputs and date pickers. Additionally, you can specify distinct colors for placeholder text, card borders, and box borders depending on whether the input appears on a light or dark background.

These new properties make it easier to map your organization's unique design system directly to your interfaces.

### Ensure continuous portal access during deployments

Version : 26.5

We've enhanced portals to keep user sessions active during deployments, just like in sites. Now, you can deploy app changes to production without interrupting portal users.

## Interfaces

### Deliver faster, more dynamic interfaces with tab layout enhancements

Version : 26.6

Build faster, more responsive interfaces with powerful new enhancements to the tab layout component. You can now take full control over performance by choosing whether to load tab contents immediately or when the tab is selected.

We're also helping you to make the navigation experience more personal for your users. You can now use the new selectedTab and selectedTabSaveInto parameters to specify which tab to load first and save information when a user clicks a tab. This allows you to automatically load specific tabs for certain users, use URL parameters to navigate directly to a tab, and more.

These updates empower you to deliver high-performance interfaces that handle complex data with ease while providing a seamless experience for your users.

### Take full control over your grid's search experience

Version : 26.6

You can now customize exactly how read-only grids search data. Use the new smartSearchType parameter to add lexical or semantic search to your grid on top of standard keyword search. Whether you're searching for exact terms or similar concepts, the smartSearchType parameter ensures you always find the most relevant results.

To further refine the experience and boost grid performance, the new searchFields parameter lets you specify exactly which fields to search. This parameter also allows you to search fields that aren't visible in the grid, like documents and extra long text fields, so your users can see a wider view of your data.

### Modernize grid designs with new styling and filter menus

Version : 26.5

We've made a series of enhancements to read-only and editable grids to provide a more intuitive and professional experience for your users.

In 26.4, we introduced new selection styling. Now, when some rows in a grid are selected, the checkbox in the grid header indicates that not all items are selected. We also improved the behavior of the search box and filters for read-only grids on ultra-wide screen monitors.

Building on those updates, the 26.5 release offers even more flexibility for your grid's display. You can now choose the new LIGHT_WITH_OUTER_BORDERS style to show only row and outer borders for more design flexibility.

Additionally, we added a new showManageFiltersMenu parameter to read-only grids so you can decide exactly when users can manage their own filters.

### More clarity for test scenarios

Version : 26.6

We've added an icon to interface test scenarios to show which scenario was last used, providing you with the context you need to efficiently test your interfaces.

### Apply colors in the styled text editor

Version : 26.4

Enable users to enhance their content with new color and highlighting options in the styled text editor . Users can now apply text and highlight colors to their content, making it simple to create more impactful and scannable content.

### More color and size options for key components

Version : 26.6

You now have more options and flexibility when configuring key components. Tags , stamps , and rich text components now support the yellow "warn" color—making them more consistent with other components. And, you also can choose a smaller stamp size for even more flexibility when designing interfaces.

### More modern disabled input styling

Version : 26.6

We've refreshed the disabled state for input components to use opacity instead of a fixed color and also unified the style across all components. This change creates a clearer visual distinction between active and disabled fields, aligns with modern design standards, and allows more flexibility for the input background color CSS properties .

### Initiate text messages directly from a mobile device

Version : 26.6

The safe link component now supports the sms: URI, so you can configure links to open directly in a device's default text messaging application.

### Performance improvements

Version : 26.6

We've optimized several components to ensure your applications remain fast and responsive. You'll see the greatest improvement when using these components in more complex designs with large amounts of data.

## Plug-ins

### Bring your data to life with the 3D Viewer

Version : 26.5

We're expanding our suite of Advanced Plug-ins with the new 3D Viewer , a cutting-edge component that lets you embed and interact with 3D models directly in your interfaces. Supporting over 15 industry-standard formats, this tool allows users to rotate, zoom, and even explode models for easy inspection. By bringing spatial data into your workflows, you can empower your users to make faster, more informed decisions without ever leaving Appian.

### Streamline plug-in development with the enhanced Plug-in SDK

Version : 26.4

We've updated the Appian Plug-in SDK to include all necessary public API classes, eliminating the search for missing files. And, to accelerate project setup even more, the SDK is now available on Maven Central . These enhancements remove development friction so you can focus on delivering high-impact solutions with ease.

### Build more accessible custom components

Version : 26.4

Deliver a more inclusive experience with your component plug-ins , thanks to our new ARIA attribute APIs . Use the Appian.Component.getAriaLabelledBy() and Appian.Component.getAriaDescribedBy() methods to ensure screen readers announce the labels, instructions, and validation message so that all users can access the information.

## Case Management Studio

### Orchestrate external cases with our web API library

Version : 26.6

We've made it easier than ever to connect Case Management Studio to your external systems with our new library of Web API templates.

These pre-built templates let you programmatically create, update, and retrieve case data—like comments and documents—directly from your external or legacy tools. And, by natively supporting the custom fields and logic you've already configured in the Control Panel, our new APIs keep your systems in sync and secure.

This streamlined approach slashes development time and cuts out manual data entry, so your case workers can focus on resolving cases and hitting those SLA targets.

### Discover information faster with AI Smart Search for documents

Version : 26.4

Find critical information across your Workspace with the power of AI. The AI Smart Search module now indexes the content of your case documents alongside case and task data, enabling you to find the right case, task, or document based on context and meaning—no need to remember exact file names or phrases.

With these updates to the AI Smart Search module, you can quickly find the resources you need, making your case management process more efficient and effective.

### Accelerate sequential task transitions with lightning speed

Version : 26.6

Boost your productivity with faster transitions between critical tasks. We've optimized our underlying workflow logic to slash the time between clicking "Complete" and having your next task ready to work. By reducing backend latency and consolidating record writes into a single expression rule, we've cut process overhead to dramatically reduce the time between task handoffs. These enhancements ensure your most complex automated workflows provide a seamless and scalable experience as your data grows.

### Optimized performance in Case Management interfaces

Version: 26.6

We've optimized record queries and grid components to return only the exact fields your interfaces need, reducing load times and improving interface responsiveness. These performance optimizations mean less maintenance overhead for your teams and a faster, more dependable experience for your users.

## Offline Experiences

### Extend your offline experiences to Windows devices

Version : 26.6

We're opening up your offline experiences to more devices with Appian for Windows , a new desktop application that can be installed on Windows 11 devices. Workers can now view data and complete rich, dynamic forms directly from their Windows laptops or tablets without an internet connection. Best of all, any offline interfaces you've already built for Appian Mobile work on the Windows app out of the box—zero additional development effort needed!

### Experience more reliable offline form interactions

Version : 26.6

We've enhanced the way your progress is saved and managed in offline forms to prevent data loss. When you submit, save a draft, or discard changes on an offline form, you will now see a loading indicator that confirms your request is being processed. This provides immediate visual feedback and helps prevent data errors, giving you peace of mind that your work is saved correctly every time.

## Administration

### Identify and resolve frontend performance bottlenecks with Trace Explorer

Version : 26.5

Pinpoint performance bottlenecks in your interfaces, sites, and reports with Trace Explorer , a new self-service diagnostic tool for Appian Cloud environments. Available to administrators and developers in the environment-level Monitor view, Trace Explorer maps technical trace data to design objects—eliminating the need for manual log analysis or support cases. Use intuitive charts to visualize performance hotspots and analyze component-level response times to precisely optimize your front-end experiences. With direct access to actionable performance data, delivering a high-performance experience for your users is easier than ever.

### Customize your Forgot Password emails

Version : 26.6

You can now tailor Forgot Password emails to match your organization's brand, tone, and compliance requirements. Customization includes the option to create unique messages for each locale supported by your environment, giving each user cohort a more personalized experience.

We've also built in placeholders to dynamically include vital information alongside your custom content. By customizing your site's emails in the Admin Console, you ensure that these messages align with your standards and speak clearly to your users.

### Monitor application performance with Dynatrace

Version : 26.4

Maximize the performance of your mission-critical applications with support for Dynatrace. If you use Dynatrace, a third-party observability platform, you can now enable it directly from the Admin Console to gain a unified view of your application health. This deeper visibility helps you identify and resolve bottlenecks faster, ensuring a consistently high-quality experience for your users.

### Stream your logs to Amazon S3

Version : 26.4

Monitoring your Appian Cloud environment is more flexible than ever. This release, we've expanded our log streaming capabilities to include support for Amazon S3 . With minimal setup in the Admin Console, you can easily stream logs directly to your own S3 buckets, giving you more control over how you retain and analyze data about your Appian environment.

### Take control with self-service alerts

Version : 26.4

Note: This feature is available as a preview. Preview features are fully supported; however, they do not reflect the full functionality or performance of the feature yet.

We've introduced a new Self-Service Alerts dashboard in MyAppian that gives support contacts immediate visibility into issues affecting your Appian Cloud environment, such as long-running database transactions. A new banner in the Support page will also give a heads-up on any active alerts.

Plus, support contacts will receive email messages containing clear, actionable steps to resolve these issues at their own pace.

With these self-service tools, it's easier than ever to maintain a healthy environment for your organization.

### Enforce terms of service for SSO sign-ins

Version : 26.5

Administrators can now enforce mandatory terms of service (ToS) for all users authenticating with single sign-on (SSO), including SAML 2.0 and OpenID Connect (OIDC). This ensures that all users must acknowledge the terms before gaining access to the application, regardless of the identity provider (IdP) used for authentication.

### Enhanced Business Continuity now available in all regions

Version : 26.4

Environments in all Appian Cloud regions are now eligible for Enhanced Business Continuity. Enhanced Business Continuity stores backups of your production environment in a secondary region for the purpose of disaster recovery. This ensures that if there is a region-wide disaster that impacts operations in your environment's primary region, such as an earthquake or hurricane, your data will be available in a secondary region and your environment can be restored there. Previously only certain regions were eligible for this offering.

Enhanced Business Continuity is available as a separate purchase to customers on the Professional and Signature Success Plans .

## Logging

Each release, we had new logs to help you track and examine your applications.

### 26.5 logs

Version : 26.5

- tos-audit.csv - Records when a user accepted or rejected the terms of service agreement, the version of the terms of service text, the user's authentication type (native, OpenID Connect, PIEE, or SAML), and other details such as IP address and user agent.

- tos-audit-version-mapper.csv - Maps the version identifier shown in the tos-audit.csv to the full text of the terms of service shown to a user.

### 26.4 logs

Version : 26.5

Three new performance logs have been added to let you examine activity chaining in autoscaled processes:

- epex_chain_trace.csv

- epex_chain_details.csv

- epex_chain_summary.csv

## General resolved issues

### 26.6 General resolved issues

Version : 26.6

- DR-8514 - Medium Fixed inconsistent refresh behavior after form submission in the Appian Mobile app.

- LCP-35431 - Medium Fixed an issue where SharePoint and other Connected System integrations experienced authorization failures due to stale user contexts following user deactivation or renaming.

- LCP-42643 - Medium Fixed an issue with startup performance caused by the translations system record type when multiple locales are configured.

- LCP-2428 - Low Fixed an issue to remove an error incorrectly logged in the debug logs.

### 26.5 General resolved issues

Version : 26.5

- LCP-28445 - Medium Expression editor autosuggest now works correctly when a colon exists on the current line.

- LCP-35274 - Low Viewing a timer configuration no longer incorrectly marks the process model as edited.

- LCP-35257 - Low Process variables used only in MNI configuration are no longer incorrectly flagged as unused.

- LCP-22292 - Low Hidden accessibility text is no longer included when copying and pasting component labels.

### 26.4 general resolved issues

Version : 26.4

- LCP-35417 - Low Fixed an issue where downloading PDF files from Tempo news posts incorrectly appended "(version 1)" to the file name.

- LCP-35346 - Low Fixed an issue in the Process Modeler where the Operator and Target values in script task custom outputs appeared corrupted after saving and reopening the node when using the "is stored at index" operator.

- LCP-35305 - Low Fixed an issue where the scrollbar disappeared in the Process Details after updating a process variable value.

- LCP-35224 - Low Fixed an issue where the Password tab in User Settings should remain hidden when a Remember Me token was used to authenticate the user during sign in.

## Accessibility resolved issues

### 26.5 Accessibility resolved issues

Version : 26.5

- LCP-52312 - Medium Dropdown selection ticks and hover states are now visible with Windows high contrast themes enabled.

- LCP-41281 - Medium Checkbox, toggle, date picker, and date time picker selected/disabled states are now visible with Windows high contrast themes.

## Behavior changes

This section describes behavior changes that impact how you previously used or interacted with an existing feature, functionality, or the platform in an earlier version. This includes any changes that require you to modify your application after upgrading to the latest version of Appian.

### Reuse old process IDs in standard processes

Version : 26.6

In a future release, the standard process execution engine will reclaim unused process IDs after six months. This change will ensure uninterrupted processing of your high-volume workflows by assigning these IDs to new process instances when needed.

Reach out to your Account Executive for more information.

### New Appian.Component.onNewValue() triggers for component plug-ins

Version : 26.4

The Appian.Component.onNewValue() JavaScript API now triggers when the instructions or validations parameters change. Previously, the only common parameters that triggered it were the required , height , and disabled parameters. Review your component plug-ins to ensure these additional parameters are handled correctly.

## Evolutions

The following components have newer, improved versions in this release. Existing, old versions in your applications will continue to function normally, but will be renamed on upgrade to indicate that they are older versions.

### Evolved AI skill smart services

Version : 26.6

We've evolved the Execute Generative AI Skill , Advanced IDP Tools , and Extract from Document smart services to include new inputs and outputs to provide execution-level visibility into AI Action usage . The previous version, which provided outputs for tokens, continues to function as normal for your existing workflows.

### Start Process smart service

Version : 26.4

The new version of the Start Process smart service and a!startProcess() fixes a bug where asynchronously starting a standard process with activity chaining caused the parent process to incorrectly wait for the child process to finish.

## Deprecations

The features listed below are deprecated and will be removed in a future release of Appian. Do not begin using deprecated features, and transition away from any prior usage of now deprecated features. Where applicable, supported alternatives are described for each deprecation.

### Non-containerized self-managed environments

For self-managed environments, Appian 25.3 was the last non-containerized version and will continue to receive hotfixes and critical updates throughout its support period . When you're ready to update, Appian on Kubernetes is the path forward for self-managed deployments.

### Minimum required Android OS for Appian Mobile

Version : 26.6

Starting in the Appian 26.9 release, the Appian Mobile Android app will increase the minimum required Android OS from Android 8 to Android 13. To align strictly with our mobile operating system support policy , Appian will begin increasing the minimum required Android OS version on an annual basis.

To maintain platform security and performance, users will need to upgrade their devices to the minimum required OS version in order to install or update the Appian Mobile app. This updates our previous policy, which permitted users to run the application on older, unsupported Android versions without active bug resolutions.

### End-of-support for older versions of RDBMS

Version : 26.5

The following relational database management systems (RDBMS) either have already reached or are approaching the standard end-of-support dates set by their vendors and will no longer be supported in a future release of Appian. Customers are strongly advised to upgrade to a newer supported version .

### Seoul Appian Cloud region

Version : 26.4

Appian Cloud is no longer accepting new customers in the Seoul region. We will remove this region in the future.


---

## Appian 26.7 — synced 2026-08-16

Source: https://docs.appian.com/suite/help/26.7/Appian_Release_Notes.html

# Appian Release Notes

Access new features and improvements every month on Appian Cloud

## Appian MCP Server

### Partner with AI to analyze process performance

Version : 26.7

Explore your process data through natural language using the Appian MCP Server . We've added process insights capabilities to the Appian MCP Server, so you can ask questions like "How long are cases taking?" or "What does our approval process look like?" and get reliable answers directly from your process data. Get to insights faster with an AI-powered analysis partner, backed by the same analytical engine and security that powers Process HQ .

## AI agents

### Power your AI agents with preferred model providers

Version : 26.7

Bring your organization's pre-approved AI model providers directly into the AI agent design object. You can link your own external cloud accounts to use your negotiated volume discounts and easily satisfy strict regulatory requirements.

A smart new Auto selection feature dynamically runs the best available model from your chosen provider, keeping your workflows current without manual updates. We're making it easier to create compliant AI agents with the exact infrastructure you want and ensure you can seamlessly swap providers as your operational needs change.

### Process complex documents using AI agents

Version : 26.7

Expand what your AI agents can see and understand with powerful new document extraction capabilities. AI agents now natively process visually complex files —like organizational charts, spreadsheets, and scanned forms—without the need for custom-built tools.

### Rapidly test chat agents

Version : 26.7

Test and refine your chat agents faster with new testing tools and flexible visual styling. The Build tab now includes a dedicated test console where you can send messages, stream responses, and inspect full chat agent timelines without needing to create an interface.

A new STOP button lets you interrupt active responses instantly in both the test console during development and in production a!agentChatField() interfaces, so end users can halt responses too.

Together, these enhancements make it easier to debug chat agents and deliver sleek, modern chat experiences to your users.

### Customize chat field styling with precision

Version : 26.7

The a!agentChatField() component now enables you to take full visual control over your chat interfaces with new shape and showBorder parameters. These parameters let you quickly configure the shape of container corners, as well as show or hide outer borders. Now you can deliver more tailored conversational experiences to your users.

## AI governance

### Expand Your AI Options with GPT 5.4 and 5.5

Version : 26.7

When you choose Appian as your cloud provider, you can now use GPT 5.4 and 5.5 to power AI experiences in Appian. These highly capable reasoning models serve as reliable alternatives to Anthropic models for your generative AI skills and a!genAiModels() function. Built on a secure foundation, this approach easily meets both strict public sector compliance and regional data residency requirements.

### Streamline model management with automatic routing

Version : 26.7

Protect automated processes from model deprecations with the new Auto option for AI skills . It dynamically routes executions to the best available Appian-recommended model—so your workflows keep running smoothly as models evolve, with no manual intervention required.

### Access live AI model limits dynamically

Version : 26.7

Scale your generative AI features across new models and providers without manual app updates. The a!genAiModels() function now retrieves live operational metadata about limits and restrictions. File size limits, page counts, and spreadsheet boundaries are all retrieved and categorized by task type. Now your apps are automatically updated with backend limit changes, so you no longer need to maintain static restrictions in your code.

## RPA

### Easily automate your core mainframe applications

Version : 9.25 (26.7)

Bring enterprise-grade support and modern efficiency to your workflows with our new native, fully supported Mainframe feature .

You can use simple drag-and-drop actions to securely connect your core legacy systems to Appian processes, while automatically handling screen timing adjustments and converting code into plain language. Now, you can effortlessly meet strict corporate security standards while ensuring your automations are highly reliable and faster to build.

### Update RPA credentials directly within robotic tasks

Version : 9.25 (26.7)

Rotate and update your RPA credentials securely without ever leaving your robotic task. The new Update Credential action writes new passwords directly to the credential store during execution using a credential UUID. By eliminating complex API calls and keeping sensitive data entirely within the robotic task, you can now implement fully automated, end-to-end credential rotation workflows with complete confidence.

### Revert your RPA infrastructure topologies safely

Version : 9.24 (26.6)

Appian Cloud RPA sites can now be reverted from a Highly Available (HA) topology to a single-node configuration when required, such as for troubleshooting or broader topology changes. Appian Support manages the transition, and your existing agents, robots, and robotic tasks continue to function without manual updates.

## Deployments

### Deploy larger database script files

Version : 26.7

We've dramatically increased the supported file sizes for database scripts in your deployments, now up to 100 MB per package! This increase ensures that your deployment capabilities are flexible and reliable enough to support complex, cross-application releases with absolute confidence.

### Improved readability for object comparisons

Version : 26.7

We've added the intuitive and easy-to-read object references you know and love directly into the object comparison view . Now, you can know exactly which objects are being referenced at a glance, providing you with a more streamlined version management experience and deployment workflow.

## Data fabric

### Richer record type metadata with a!recordTypeProperties()

Version : 26.7

The a!recordTypeProperties() function now returns additional metadata to give you deeper visibility into your data architecture. Each record type result now includes an applications property, which tells you which apps your record type belongs to. We've also added commonField and commonFieldType values to the relationships property, so you can see how the two record types are connected. These enhancements enable you to use more of your record type metadata throughout your apps and processes.

## Integrations

### Sync records when consuming Kafka events

Version : 26.7

Keep your synced record types up to date the instant data changes by using a!syncRecords() in your event consumers . Instead of building a process model to trigger syncs, you can now tell Appian to fetch the latest data right in the event handler expression. This lightweight approach reduces architectural complexity and delivers fresher data for your applications.

### Event consumer performance improvements

Version : 26.7

We've optimized how event consumers process incoming Kafka events, delivering up to 5x faster throughput and reduced latency for your event-driven workflows. These improvements happen automatically—no configuration required!

### Securely connect to Kafka brokers with JWT bearer tokens

Version : 26.7

Kafka connected systems can now use the JWT bearer authorization grant for SASL and SASL_SSL connections. As part of a zero-trust setup connecting Appian and your broker, this server-to-server authentication type lets you enable two-way SSL. This update gives you even more flexibility in securely integrating Appian with Kafka.

### Stream your event consumer logs

Version : 26.7

You can now stream the following event consumer logs to your own systems using Amazon S3 :

- event_consumer_details.csv

- event_consumer_summary.csv

- event_consumer_errors.csv

- event_consumer_events_errors.csv

- event_consumer.csv

## Process modeling and autoscale

### Model processes in your preferred language

Version : 26.7

The process modeler now uses your locale setting to display labels and UI elements in your preferred language. Enjoy a better process modeling experience and boosted development efficiency for global teams.

## Process HQ

### Unify your dashboard view with date filters and saved defaults

Version : 26.7

Comparing data across your dashboard just got easier. In addition to dataset-based reports, you can now apply dashboard date filters to process KPIs and process-based reports .

Now, users can select a custom date range, and every item on the dashboard will reflect the same time period at a glance. You can also set default filter values so viewers see a meaningful starting point the moment they open your dashboard.

Together, these updates give you more control over your dashboard experience and help your business users get to insights faster.

### Focus your process calculations with a working schedule

Version : 26.7

When you're monitoring SLA compliance or optimizing your business process , you need your duration calculations to be as accurate as possible. We're adding the ability to exclude weekends from duration calculations, so the time spent on each task reflects your organization's working hours.

### Sort report grids while viewing a dashboard

Version : 26.7

We've added the ability for report viewers to sort grid columns directly from a dashboard . Click any column header to quickly organize your data in ascending or descending order.

### Access insights quickly with more performant dashboards

Version : 26.7

We've enhanced the performance of Process HQ dashboards , resulting in initial load times that are up to 50% faster and subsequent interactions that are up to 36% faster. This speed boost accelerates your business users' ability to make data-driven decisions by allowing them to swiftly analyze and interact with critical reports.

## Interfaces

### Visually explore your data relationships

Version : 26.7

Introducing the Record Knowledge Graph component , an interactive graph that lets you visually explore how your records connect across your applications. Simply specify a starting record and the depth of nested relationships to instantly see all of its related records. Now, your users can seamlessly navigate through complex data models and see the big picture at a glance.

### More flexible tab layouts with vertical orientation, async loading, and new tab widths

Version : 26.7

Designing secondary navigation for your interfaces just got a whole lot faster with new vertical orientation for tab layouts ! Instead of manually building vertical navigation from scratch, you can now effortlessly build it in seconds.

Plus, you can now choose to load tabs asynchronously in the background, so data-heavy tabs don't slow down the initial page load.

And, to give you even more flexibility, we've also added the ability to distribute horizontal tabs evenly across the tab bar.

With these robust new styling options, you can quickly craft sleek, modern interfaces that align with your brand.

### Design polished interfaces with expanded styling controls

Version : 26.7

Build beautiful, brand-aligned applications with more precision than ever. We're giving you more control over the styling of some of our most popular components, allowing you to effortlessly design user experiences perfectly tailored to your brand.

Establish a clear visual hierarchy and match your organization's exact typography guidelines using our new font weight options. You now have more granular control over the font weight of rich text , with the addition of light and semi-bold font weights. We're also making box and section layouts more flexible by giving you control over the label font weight.

Additionally, you can quickly add emphasis to box and card layouts by adjusting the border thickness, or draw the user's eye by configuring the border color of box layouts.

### Accelerate and streamline your interface testing workflow

Version : 26.7

Now, there's a simpler way to configure test values for rule inputs in interfaces. You can easily save test values as a new or existing test scenario without navigating to the Manage Test Scenarios screen. This seamless experience eliminates context switching, allowing you to test and refine your interfaces without breaking your flow.

### Enhanced legibility for the signature component

Version : 26.7

We've made the pen stroke in the signature component more prominent to ensure that all signatures are crisp and easy to read. Now, your users can verify signed documents more quickly.

### Updated Appian SAIL Component Library in Figma

Version : 26.7

We've released a new version of the Appian SAIL Component Library in Figma with additional components and new component styles. If your team already uses the library, download the latest version to access the updates.

While mocking up SAIL UIs directly in Appian will always be the most efficient way to iterate on your designs, this resource provides flexibility for teams who already use Figma.

### Component performance improvements

Version : 26.7

This release, we've optimized several components to ensure your applications remain fast and responsive. You'll see the greatest improvement when using these components in more complex designs with large amounts of data. Learn more about interface performance .

## Sites and Portals

### Take control of buttons with new CSS profile properties

Version : 26.7

We're continuing to deliver more robust CSS profile capabilities with the introduction of even more properties . These new properties allow you to easily customize button padding, font styling, minimum button width, and border width, as well as spacing between buttons. And, you can now precisely control the border radius of card and box layouts. With more design options, we're making it easier to map your organization's unique design system directly to your interfaces.

## Administration

### Capture trace IDs instantly with Interaction Diagnostics

Version : 26.7

We've made it much easier to troubleshoot slow-loading front-end design objects, removing the need to use your browser's developer tools. With Interaction Diagnostics , any authenticated user can capture diagnostic trace information (including trace ID, timestamp, duration, and response code) with a single click from the navigation menu.

Once captured, the diagnostic modal displays all relevant telemetry in a single view. Click Copy to clipboard to easily share the information with your support team or use it to investigate directly in Trace Explorer .

### Securely connect to self-hosted resources with Cloud Secure Link

Version : 26.7

We're introducing Cloud Secure Link to provide private, zero-trust connectivity to your self-hosted databases and APIs. No need to open inbound firewall ports! Simply deploy our lightweight, containerized client within your network to establish an mTLS-encrypted reverse SSH tunnel back to Appian Cloud. Then, easily manage your connections right from the Admin Console . With Cloud Secure Link, you can connect to any cloud service provider or on-premises architecture while maintaining absolute network isolation.

### Pre-configure cross-region connections for optimized disaster recovery

Version : 26.7

Appian Cloud now supports cross-region PrivateLink for Enhanced Business Continuity. In cooperation with Appian Support, you'll be able to pre-configure cross-region PrivateLink connections in your secondary Appian Cloud region ahead of time. In the event of a regional failover, your inbound and outbound integrations can smoothly transition without requiring you to manually update hostnames or reconfigure your endpoints. Experience faster recovery times and complete peace of mind knowing your critical business operations remain connected and uninterrupted.

### Tailor the sign-out experience for your users

Version : 26.7

Keep your users in the flow of their work, even after their session ends. You can now configure Appian to automatically return users to their last visited page when they sign back in, allowing them to seamlessly resume their work without losing valuable context. This new behavior will apply by default to new environments; existing environments will need to manually enable this in the Admin Console .

To further unify your app for users, you can also replace the default "Return to Appian" text on the sign-out page with custom phrasing to match your organization's identity.

Tailor these simple authentication settings to provide a polished experience that helps everyone work more efficiently.

### Defer MFA app enrollment for flexible onboarding

Version : 26.7

Streamline account setup and give your users the flexibility to enroll in multi-factor authentication (MFA) when they are ready. With a new configuration in the Admin Console , users can defer setting up their authenticator app during their first sign-in and log in immediately. When they are ready, they can quickly complete their security setup directly from their user profile.

### Stream your AI guardrail violation logs

Version : 26.7

You can now stream AI guardrail violation logs to your own systems using Amazon S3 or syslog receivers .

## General resolved issues

- AP-52320 - Medium Appian now correctly handles special Unicode characters in process variables by encoding them as valid XML character references, preventing previous serialization failures. 26.6 General resolved issues

### 26.6 General resolved issues

Version : 26.6

- DR-8514 - Medium Fixed inconsistent refresh behavior after form submission in the Appian Mobile app.

- LCP-35431 - Medium Fixed an issue where SharePoint and other Connected System integrations experienced authorization failures due to stale user contexts following user deactivation or renaming.

- LCP-42643 - Medium Fixed an issue with startup performance caused by the translations system record type when multiple locales are configured.

- LCP-2428 - Low Fixed an issue to remove an error incorrectly logged in the debug logs.

### 26.5 General resolved issues

Version : 26.5

- LCP-28445 - Medium Expression editor autosuggest now works correctly when a colon exists on the current line.

- LCP-35274 - Low Viewing a timer configuration no longer incorrectly marks the process model as edited.

- LCP-35257 - Low Process variables used only in MNI configuration are no longer incorrectly flagged as unused.

- LCP-22292 - Low Hidden accessibility text is no longer included when copying and pasting component labels.

### 26.4 general resolved issues

Version : 26.4

- AP-44361 - Medium Fixed broken process diagram layout in Firefox browser.

- LCP-35417 - Low Fixed an issue where downloading PDF files from Tempo news posts incorrectly appended "(version 1)" to the file name.

- LCP-35346 - Low Fixed an issue in the Process Modeler where the Operator and Target values in script task custom outputs appeared corrupted after saving and reopening the node when using the "is stored at index" operator.

- LCP-35305 - Low Fixed an issue where the scrollbar disappeared in the Process Details after updating a process variable value.

- LCP-35224 - Low Fixed an issue where the Password tab in User Settings should remain hidden when a Remember Me token was used to authenticate the user during sign in.

## Accessibility resolved issues

- AP-52312 - Medium Multiple dropdown selection ticks and hover states are now visible with Windows high-contrast themes enabled.

AP-52312 - Medium Multiple dropdown selection ticks and hover states are now visible with Windows high-contrast themes enabled.

- AP-38419 - Medium Keyboard focus indicators are now visible on frozen sortable grid headers.

AP-38419 - Medium Keyboard focus indicators are now visible on frozen sortable grid headers.

- AP-35518 - Low Keyboard focus indicators are now visible on ellipsis icons in multiple dropdowns.

AP-35518 - Low Keyboard focus indicators are now visible on ellipsis icons in multiple dropdowns.

## Evolutions

The following components have newer, improved versions in this release. Existing, old versions in your applications will continue to function normally, but will be renamed on upgrade to indicate that they are older versions.

### Evolved card group layout component

Version : 26.7

We've evolved the card group layout component with enhancements to the fillContainer parameter. These enhancements allow card group contents to more intuitively fill the width of a container without stretching beyond a configurable limit.

## Deprecations

The features listed below are deprecated and will be removed in a future release of Appian. Do not begin using deprecated features, and transition away from any prior usage of now deprecated features. Where applicable, supported alternatives are described for each deprecation.

### Non-containerized self-managed environments

For self-managed environments, Appian 25.3 was the last non-containerized version and will continue to receive hotfixes and critical updates throughout its support period . When you're ready to update, Appian on Kubernetes is the path forward for self-managed deployments.

## Removals

The features listed below have been removed from Appian and can no longer be used.

### Custom domain certificates transition to managed service

Version : 26.7

The Certificates page has been removed from MyAppian because Appian Cloud does not currently support self-service for custom domain certificates. Instead, you can configure and renew custom domain certificates with assistance from Appian Support .
