# Appian Handbook

Auto-updated from public Appian release notes (docs.appian.com). Not affiliated with or endorsed by Appian Corporation. Content is sourced from Appian's own public documentation; see each section's source link for the original.

---

## Appian 25.3 — synced 2026-08-14

Source: https://docs.appian.com/suite/help/25.3/Appian_Release_Notes.html

Highlights from this release, summarized:

- **Process HQ on your Site** — the Reports and Dashboards Library can now be embedded as a page inside an Appian Site, with light/dark theming and custom branding.
- **Appian Composer (preview)** — an AI-assisted planning tool that turns a plain-language description into a working app scaffold (groups, interfaces, record types, landing page).
- **Async interface loading** — the new `a!asyncVariable()` function lets slow-loading data load independently of the rest of the UI, improving perceived performance.
- **Self-managed AI** — AI Copilot and AI skills are now available for self-managed (Kubernetes) environments, not just Appian Cloud.
- **Smart search GA** — semantic search now returns more matches, supports larger datasets, and includes better error/indexing diagnostics.
- **AI skills** — Advanced IDP Tools now supports query-based extraction ("what is the patient's name?") and image file inputs (JPEG/PNG/TIFF).
- **Data fabric** — scheduled incremental syncs now extend to database-backed record types; new document monitoring/cleanup tools; expanded related-record query limits (up to 250 for `queryByIdentifier`).
- **Interfaces** — new sidebar template for forms/wizards, accessible message banner component, transparent hex color support, and a faster, more responsive design-mode experience.
- **Admin** — trusted server certificates now work automatically with OpenID Connect; the `configure.sh` script has moved to a standalone download on Forum.
- **Deprecations** — legacy RPA Queues/Scheduling are deprecated (full removal in 26.1); report objects can no longer be added directly as Site pages.

*(Once you run the automated workflow, newer releases — 25.4, 26.1, 26.3, 26.6, 26.7, etc. — will be appended below this section automatically.)*


---

## Appian 26.7 — synced 2026-08-16

Source: https://docs.appian.com/suite/help/26.7/Appian_Release_Notes.html

# Appian Release Notes

Share via

LinkedIn

Reddit

Email

Copy Link

Print

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

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Process complex documents using AI agents

Version : 26.7

Expand what your AI agents can see and understand with powerful new document extraction capabilities. AI agents now natively process visually complex files —like organizational charts, spreadsheets, and scanned forms—without the need for custom-built tools.

### Rapidly test chat agents

Version : 26.7

Test and refine your chat agents faster with new testing tools and flexible visual styling. The Build tab now includes a dedicated test console where you can send messages, stream responses, and inspect full chat agent timelines without needing to create an interface.

A new STOP button lets you interrupt active responses instantly in both the test console during development and in production a!agentChatField() interfaces, so end users can halt responses too.

Together, these enhancements make it easier to debug chat agents and deliver sleek, modern chat experiences to your users.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Customize chat field styling with precision

Version : 26.7

The a!agentChatField() component now enables you to take full visual control over your chat interfaces with new shape and showBorder parameters. These parameters let you quickly configure the shape of container corners, as well as show or hide outer borders. Now you can deliver more tailored conversational experiences to your users.

## AI governance

### Expand Your AI Options with GPT 5.4 and 5.5

Version : 26.7

When you choose Appian as your cloud provider, you can now use GPT 5.4 and 5.5 to power AI experiences in Appian. These highly capable reasoning models serve as reliable alternatives to Anthropic models for your generative AI skills and a!genAiModels() function. Built on a secure foundation, this approach easily meets both strict public sector compliance and regional data residency requirements.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Streamline model management with automatic routing

Version : 26.7

Protect automated processes from model deprecations with the new Auto option for AI skills . It dynamically routes executions to the best available Appian-recommended model—so your workflows keep running smoothly as models evolve, with no manual intervention required.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

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

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

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

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

## Process HQ

### Unify your dashboard view with date filters and saved defaults

Version : 26.7

Comparing data across your dashboard just got easier. In addition to dataset-based reports, you can now apply dashboard date filters to process KPIs and process-based reports .

Now, users can select a custom date range, and every item on the dashboard will reflect the same time period at a glance. You can also set default filter values so viewers see a meaningful starting point the moment they open your dashboard.

Together, these updates give you more control over your dashboard experience and help your business users get to insights faster.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Focus your process calculations with a working schedule

Version : 26.7

When you're monitoring SLA compliance or optimizing your business process , you need your duration calculations to be as accurate as possible. We're adding the ability to exclude weekends from duration calculations, so the time spent on each task reflects your organization's working hours.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

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

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### More flexible tab layouts with vertical orientation, async loading, and new tab widths

Version : 26.7

Designing secondary navigation for your interfaces just got a whole lot faster with new vertical orientation for tab layouts ! Instead of manually building vertical navigation from scratch, you can now effortlessly build it in seconds.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

Plus, you can now choose to load tabs asynchronously in the background, so data-heavy tabs don't slow down the initial page load.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

And, to give you even more flexibility, we've also added the ability to distribute horizontal tabs evenly across the tab bar.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

With these robust new styling options, you can quickly craft sleek, modern interfaces that align with your brand.

### Design polished interfaces with expanded styling controls

Version : 26.7

Build beautiful, brand-aligned applications with more precision than ever. We're giving you more control over the styling of some of our most popular components, allowing you to effortlessly design user experiences perfectly tailored to your brand.

Establish a clear visual hierarchy and match your organization's exact typography guidelines using our new font weight options. You now have more granular control over the font weight of rich text , with the addition of light and semi-bold font weights. We're also making box and section layouts more flexible by giving you control over the label font weight.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

Additionally, you can quickly add emphasis to box and card layouts by adjusting the border thickness, or draw the user's eye by configuring the border color of box layouts.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Accelerate and streamline your interface testing workflow

Version : 26.7

Now, there's a simpler way to configure test values for rule inputs in interfaces. You can easily save test values as a new or existing test scenario without navigating to the Manage Test Scenarios screen. This seamless experience eliminates context switching, allowing you to test and refine your interfaces without breaking your flow.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Enhanced legibility for the signature component

Version : 26.7

We've made the pen stroke in the signature component more prominent to ensure that all signatures are crisp and easy to read. Now, your users can verify signed documents more quickly.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

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

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

## Administration

### Capture trace IDs instantly with Interaction Diagnostics

Version : 26.7

We've made it much easier to troubleshoot slow-loading front-end design objects, removing the need to use your browser's developer tools. With Interaction Diagnostics , any authenticated user can capture diagnostic trace information (including trace ID, timestamp, duration, and response code) with a single click from the navigation menu.

Once captured, the diagnostic modal displays all relevant telemetry in a single view. Click Copy to clipboard to easily share the information with your support team or use it to investigate directly in Trace Explorer .

### Securely connect to self-hosted resources with Cloud Secure Link

Version : 26.7

We're introducing Cloud Secure Link to provide private, zero-trust connectivity to your self-hosted databases and APIs. No need to open inbound firewall ports! Simply deploy our lightweight, containerized client within your network to establish an mTLS-encrypted reverse SSH tunnel back to Appian Cloud. Then, easily manage your connections right from the Admin Console . With Cloud Secure Link, you can connect to any cloud service provider or on-premises architecture while maintaining absolute network isolation.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Pre-configure cross-region connections for optimized disaster recovery

Version : 26.7

Appian Cloud now supports cross-region PrivateLink for Enhanced Business Continuity. In cooperation with Appian Support, you'll be able to pre-configure cross-region PrivateLink connections in your secondary Appian Cloud region ahead of time. In the event of a regional failover, your inbound and outbound integrations can smoothly transition without requiring you to manually update hostnames or reconfigure your endpoints. Experience faster recovery times and complete peace of mind knowing your critical business operations remain connected and uninterrupted.

### Tailor the sign-out experience for your users

Version : 26.7

Keep your users in the flow of their work, even after their session ends. You can now configure Appian to automatically return users to their last visited page when they sign back in, allowing them to seamlessly resume their work without losing valuable context. This new behavior will apply by default to new environments; existing environments will need to manually enable this in the Admin Console .

To further unify your app for users, you can also replace the default "Return to Appian" text on the sign-out page with custom phrasing to match your organization's identity.

Tailor these simple authentication settings to provide a polished experience that helps everyone work more efficiently.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

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

## Feedback


---

## Appian 24.3 — synced 2026-08-16

Source: https://docs.appian.com/suite/help/24.3/Appian_Release_Notes.html

# Appian Release Notes

Share via

LinkedIn

Reddit

Email

Copy Link

Print

24.3 Release Highlights

Join our Appian Community team and other Appian experts as they dig into highlights from the 24.3 release.

Join our Appian Community team and other Appian experts as they dig into highlights from the 24.3 release.

## Release highlights

This release introduces many new and exciting features throughout the platform that make it faster to understand, interact with, and explore data across your applications. We're particularly excited to shine a spotlight on three standout features this release: Appian AI Copilot insights into your data fabric in Process HQ, expanded chat capabilities in Enterprise Copilot, and AI generated views in process insights.

### Propel your data exploration with powerful knowledge discovery

Our latest AI Copilot updates empower you to access and understand even more of your enterprise data, with plain language and fewer steps.

#### Easily find and understand scores of information with AI Copilot for data fabric

Note: This feature is available as a preview. Preview features are fully supported; however, they do not reflect the full functionality or performance of the feature yet.

With this release, AI Copilot helps you get real-time insights into even more areas of your data fabric . Now, you can ask AI Copilot questions about your whole data catalog in Process HQ, giving you more information about your enterprise data and helping you to make more informed decisions. As always, you don't need to use any code to leverage AI capabilities—just ask your question using natural language. AI Copilot not only answers your question, but also lets you know how and where it found the information in your data fabric, ensuring trust and accuracy.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

#### Find answers across all knowledge sets in Enterprise Copilot

We've made it even easier for you to chat with your knowledge sets. Our new All Knowledge Sets option lets you start chatting without selecting a knowledge set first— Enterprise Copilot will understand what you need regardless of the question. For more focused queries, simply choose the knowledge set you need. This update makes information more accessible, saving you time and letting you focus on your work.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Jump-start view creation with AI suggestions

An important step towards exploring your enterprise data in Process HQ is to create a view . But knowing which KPIs, details, and filters to choose can be intimidating and time-consuming.

Using AI Copilot, we've made it easier to create views so you can spend less time configuring your process and more time exploring your data. Users with any level of experience can benefit from views suggested by AI Copilot. New users are guided and inspired, while experienced users create views more quickly and minimize tedious work.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

AI Copilot uses what it knows about your process data to provide multiple suggestions for new views. As you explore each suggested view, you'll also see the suggested KPIs, process details, and filters. And, these suggestions are editable, so you can modify them to best fit your needs. Don't see any view suggestions you want to use? No problem—just ask AI Copilot to generate additional suggestions!

## Automation

Automation combines people, technologies, and data into a streamlined and unified workflow. Tackle a variety of business challenges so you can free up your human workforce to focus on more impactful work.

In this release, we've expanded the regional availability for AI skills and Enterprise Copilot, bringing these powerful tools to more people. AI Copilot provides faster, more continuous responses as you ask for report insights within Process HQ, and AI-generated test cases support more detailed input types.

### Multiple AI features HITRUST certified

We're happy to announce that AI Copilot and AI Skill features now meet HITRUST certification requirements:

AI Skills

- AI skills for document processing ( document extraction , document classification , email classification )

- Generative AI skills

AI Copilot for users

- Records chat component

- AI Copilot for data fabric

- Enterprise Copilot

AI Copilot for developers

- Create sample data

- Generate test cases

HITRUST certification is a comprehensive security framework that provides a standardized and rigorous approach to managing risk and protecting sensitive information, including compliance with HIPAA.

### AI Skills

#### Generative AI skills now available in five new regions

This release expands the regional availability of the prompt builder AI skill to include Canada (ca-central-1), Ireland (eu-west-1), London (eu-west-2), Sao Paulo (sa-east-1), and Mumbai (ap-south-1). Customers in unsupported regions can opt in and choose which region their data is sent to for processing. All you need to do is work with Appian Support to enable this feature.

### Appian AI Copilot for business users

We're excited to share additional AI Copilot features for business users, in addition to those highlighted above .

#### Real-time, faster report chats in data fabric insights

We're committed to continually improving the experience of chatting with AI Copilot for reports , and this release, AI Copilot responses are faster than ever. Instead of waiting for a full answer, you can see real-time updates as they become available, making for a more natural conversation. No delays—just seamless discussions.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

#### Use feedback to drive Enterprise Copilot forward

Understanding how your teams use Enterprise Copilot is key to making sure it works best for your business. Now you can do just that with our new feedback tool that's built right in. Users can provide feedback on specific knowledge sets, the overall experience, and even rate responses as good or bad.

And you can rest assured all comments are only visible to the relevant Enterprise Copilot admins and knowledge set admins within your organization. With these valuable insights, we're enabling you to make meaningful and informed improvements for those that use Enterprise Copilot every day, while still ensuring privacy for your users.

#### Expand where you use Enterprise Copilot

We want to make it easier for more people and teams to work together productively. So, we added Europe (Frankfurt) (eu-central-1) as a supported region for Enterprise Copilot allowing more of our customers in Europe to benefit from AI-powered document discovery. For a complete list of supported regions, see the Security and Compliance information.

### Appian AI Copilot for developers

#### Experience the full release of AI-generated test cases for expression rules

Previously available as a preview, we are excited to announce the full release of our AI-driven test case generation feature for expression rules. With this release, we've made it possible for you to generate test cases for all expression rules, including those with detailed inputs like maps, CDTs, and record types. Simplify your test creation and enhance your efficiency with this fully released version of AI-driven test case generation.

### RPA

#### Manage version history for robotic tasks

Version history for robotic tasks is now available! Easily explore and restore past versions, update to the latest, or delete unnecessary ones—all in Appian Designer. This addition brings a unified experience with other Appian objects, making it easier to keep your robotic tasks organized and current.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

#### Boost performance for faster automation

We've enhanced Appian RPA to speed up execution of your robotic tasks. Our improvements reduce the time it takes for a robotic task to complete by 15% or more, enhancing the efficiency of task assignment, enabling more robots to work simultaneously and better utilize available robot capacity. This improvement is especially beneficial during peak workloads when thousands of tasks need to be executed simultaneously, or in environments with more than 50 robots.

#### Java 17 is here

Beginning with RPA 9.12 (released on August 2), agents now require the use of Java 17. To ensure RPA continues to operate smoothly, upgrade to Java 17 immediately if you have not already. All low-code actions within Appian RPA are backward compatible, but you will need to check the compatibility of any custom actions. Be sure to review the Java 17 Upgrade Guidance for complete information. For help, contact Appian Support.

## Process HQ

Combining the latest technologies in data fabric, process mining, machine learning, and generative AI, Process HQ gives business users the power to explore data and identify timely insights they can use to optimize their business.

We've added new, groundbreaking enhancements to both of Process HQ's key capabilities: process insights and data fabric insights . Not only that, we've added more data governance features that make it quick and easy to secure enterprise data directly in Process HQ.

### Process insights

We're making it faster and easier for business users to go from raw data to actionable insights. Data stewards will have more options when creating processes, so data preparation takes less time than ever with less developer involvement, allowing faster iterations in your production environment.

In addition, a streamlined exploration and investigation flow makes analysts' lives easier. We now offer AI-powered view generation , investigations that start directly from KPIs and target slow activities, and a boosted collaboration experience.

#### Curate and prepare your process data in one centralized place

This release, we've made it even easier to prepare your process data in process insights .

We've added filtering to processes to help you focus your data on a specific time frame, remove unnecessary information, and optimize performance. With these new filters, data stewards can customize case and event data directly from process insights.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

Data stewards can refine and standardize the names of activities in a process using the new Find and Replace custom attribute template. Often, in raw data, activity names can be inconsistent or cluttered with dynamic details. With just a few clicks, you can create a custom attribute that optimizes your data for an improved analysis experience.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

With these new data preparation tools built directly into process insights, it's easier than ever for data stewards to help business users focus on the data that matters most.

#### Investigate the activities really slowing your process down

We're also improving investigations into activity duration, providing a new method for analyzing event data that includes both start and end timestamps.

Process insights already empowers you to track activity duration with a custom KPI . Now, you can explore activity duration as another dimension of an investigation . This allows you to look closely at how long each activity is taking and why it might be taking longer in the context of other characteristics of the process.

With this new method, you can zero in on precisely which activities represent the greatest potential for real improvement.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

#### Streamlined investigation flow

We've also streamlined the guided experience of investigating your process to make building insights more intuitive.

You'll see a more structured investigation workflow , so you can feel confident about the steps you should take to build an actionable insight. Plus, you can always see the duration against which the system is comparing the case or part of the case you're currently investigating. You can use this KPI to understand how potential savings are calculated and track how different findings affect that key metric.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

Once you've saved insights to an investigation, navigating to those insights is a breeze. We've simplified the format to highlight only the most relevant data for each insight. Quick actions let you rename an insight or adjust the potential savings calculation directly from the list.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

We've also consolidated the results of our analysis into easy-to-access tabs , reducing the time you spend scrolling.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

Each release we aim to make uncovering process inefficiencies as fast and intuitive as possible, and these quality-of-life improvements help us do just that.

#### Drill down quickly with the searchable case list

Sometimes, a finding can surprise you. Naturally, you may want to validate what you're seeing, and now that validation is as easy as searching in the Case List tab of a process view .

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

#### Track conformance easily in the executive dashboard

Process insights gives you unprecedented visibility into the flow of activities in your process. Now, with the conformance rate KPI, you can tell us the ideal order for those activities. Then we'll calculate how many processes follow that ideal path as a simple percentage of cases, so you can quickly see how well you're meeting your own standards.

This new KPI is available in the executive dashboard , replacing the now-retired error rate KPI.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

#### Get the conversation started with enhanced collaboration

Finding an actionable insight often requires business context that may be shared among multiple people in your organization. That's why process insights provides a central space where you can collaborate with analysts and process owners.

With the enhanced comment capabilities in this release, you can fully capture conversations between stakeholders—complete with helpful metadata!

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

And you can even add a brief description to your insights, so your collaborators have the shared context they need to start improving business outcomes faster.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Data fabric insights

Data fabric insights empowers any user to explore their enterprise data and find answers to their common business questions. This release, we're giving users more ways to visualize their business data, and we've enhanced the loading experience for dashboards that contain larger grids.

#### Build data rich scatter charts

We're excited to share a new scatter chart design in the report builder. This new chart allows report creators to easily visualize relationships between data points, making it simpler to identify patterns, trends, and correlations in your data.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

#### Load grids asynchronously

Users will also notice that dashboards containing large or complex grids open more quickly. Now, grid data is fetched asynchronously in the background, so users can keep building and analyzing enterprise data without having to wait for all of the data to load at once.

### Data governance

Process HQ makes it easy for trusted users to secure enterprise data on the fly. This release, we've enhanced the Data Governance page to empower users to start securely analyzing and exploring data even faster.

#### Manage which record types are available in the Data Catalog

This release, we've made it easier to manage which record types are available in the Data Catalog . Now, data governors can show or hide record types from the Data Catalog directly from the Data Governance page—no need to edit and redeploy record types. And, with a more refined list of record types, users can more efficiently find the information they need to build data-rich reports.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

#### Preview data

We've also updated the Data Governance page with a data preview.

Now, data stewards can easily access a preview of the data in record types they're assigned to by clicking the record type name, then clicking the Data Preview tab. This visibility gives your trusted users important context to understand record data when adding processes in process insights.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

## Case Management Studio

This release, we're continuing to make Case Management Studio fit your case process needs with big enhancements to using data, more customization options, and a fleet of powerful new modules.

### Do more with your data in Case Management Studio

Since Case Management Studio is backed by Appian Records and AI Copilot, you have the best of both worlds: getting the most out of your data and Studio's easy-to-use no-code experience.

This release, a quick chat with AI Copilot can help you build your case management apps using data modeling best practices. When adding new data fields to your case categories and types, simply describe the data you want to capture and we'll recommend the data type to use. And you can see our reasoning for the recommendation and help you learn data modeling best practices as you go.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

Last release, we introduced choice list fields to Studio to make lookup and reference data even easier to use in your case categories and types. This release, we're enhancing choice list fields in Studio to allow you to add multiple options at once, as well as edit the options and mark them as active/inactive. With these efficient editing tools built right into Studio, we're helping you to easily manage your lookup data and keep it as useful and up-to-date as possible.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

And, last but not least, you can now add multiple data fields to your case categories, case types, or summary views at once. Add any and all of the fields you need in less time and fewer clicks!

### Summarize documents in your cases

Appian's private AI can help make getting up to speed on cases with Case Management Studio even faster. Our new Case Document Summary module can save you time by checking out case documents and providing a quick summary of the content. And, the new Case Comments Summary module gives you a thorough summary of all comments on a case in an easy-to-skim bulleted list. These additions help your case workers quickly get the context they need, without having to read through whole documents and comment threads to get it.

### Focused case experiences for all users

We know that some Case Management Studio users only need to view their in-progress cases and create new cases. We've created the My Cases module to let them do just that, providing those users with a focused experience that allows them to view, edit, and stay up-to-date on their cases. Case Management Studio enables you and your users to efficiently move through case workflows, no matter where users are in the process.

### Frictionless user account creation

With the Public Portal module , you can already easily allow your unauthenticated users to interact with case management apps as unregistered guests. This release, we're introducing the Public Self-Registration module . This module builds off the Public Portal module and provides a way for new unauthenticated users to register for a user account without requiring additional help from your teams. You can also use this module in perfect conjunction with the My Cases module to allow new users to access their cases and provide them with a focussed experience.

### Quickly view the tasks assigned to both you and your groups

This release, we're making it easy to see not only those tasks already assigned to you, but those available for you to pick up. Alongside the Assigned to Me list in Workspace , we've added the new Assigned to Group list that shows tasks assigned to your groups that haven't been picked up yet. Now, you can quickly see a list of your tasks and assign any new ones to yourself as needed, making sure none slip through the cracks.

### Edit case workflows—even for in-progress cases!

This release, we've added new functionality that allows case workers to make large scale, lasting changes to the workflow for any one case, even if the case is currently in-progress. Previously, case workers could only create small or one-time changes to an in-progress case. Now, case workers can add multiple tasks, add entire new task blocks, name task instances, and modify task relationships in the existing workflow for a single case—all in one action! We're helping you to make your workflows more resilient and allowing you to evolve your case process as you go.

### Update multiple cases at once

Keeping with the theme of streamlining case edits, now you can also update multiple cases in Workspace at one time. Just select as many cases as you want to edit and make the changes you need—from updating the assignee or group, to changing the status or priority, and more! Improve efficiency and remove duplicative manual steps, all at once.

### Even more form configuration options to improve your users experience

In addition to Case Management Studio's no-code design experience, we also provide a wide range of low-code configurations. This release, we're introducing six new parameters to the a!studio_wizardLayout() function that allow you to configure the names of the steps in the intake form wizard and enable your users to save drafts of intake forms. With just four simple parameters, you can further tailor your case intake process to best fit both your organization's and your users' needs.

### Make demos even more engaging with easy-to-add sample data

Now, you can eliminate manual work and quickly add realistic sample data to your case management app with sample data packs in the new Demo Data module . Data packs include both configuration and transactional data, and come complete with predefined case types, tasks, task blocks, workflows, and data fields. Our easy-to-use sample data is perfect for creating engaging demos and can even help guide you on your way to building out your own unique workflows.

## Data fabric

Appian's data fabric stitches together data from multiple systems into a single, secure data model, so you can build applications quickly.

This release, you can add and remove source data directly from your record type, foster even more collaboration in your applications using record events, and more.

### Manage source data directly from your record type

We're making some exciting changes to your record type experience. We've moved the Data Preview into its own page and added the ability to add and edit source data , directly from your record type! This is especially useful for record types that contain lookup data. Now, in just a couple of clicks, you can edit a status, update an event type, or add a new region—all from the record type.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Enable more collaboration on your records

Last release, we enhanced record events so you can collaborate on your data with colleagues more easily, adding valuable transparency to your business process. Now, we've taken collaboration to the next level by allowing users to start threaded conversations on any event on the Event History List component .

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

Since these conversations are organized in threads, the main list of events stays uncluttered and easy to read. Users can mention coworkers to ask questions and quickly loop them in on the discussion. And, now it's easy to highlight crucial details in comments with new styled text options, like bold, italics, lists, and more.

When users participate in threaded conversations, Appian automatically stores the discussion in a new Reply Thread record type. You can generate this new record type when you first configure record events, or you can easily create a new record type to store replies and update your existing record events configuration.

These enhancements to record events help teams work more efficiently and make data-driven collaboration a seamless part of their everyday workflow.

### Export query performance details to Excel

The Query Performance tab allows you to monitor record queries from any of your connected environments, so you can easily understand and optimize those queries. This release, we're allowing you to export the query details to Excel, giving you more flexibility in how you analyze record queries.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Sync filters: a new look and feel for source filters

This release, we've given source filters a new look and feel, complete with a new feature name: sync filters . Now, each filter appears in a sleek card, and you can clearly see how multiple filters are evaluated.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Reorder record-level security rules

With record-level security, you can use no-code security rules to easily specify who can see which records. This release, you can reorder security rules so you can organize your security rules more logically.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

## Total experience

Appian provides a total experience that engages internal and external users across web and mobile and allows you to build beautiful interfaces with drag-and-drop design tools. This release, we've made some great enhancements to our interface components, and improved performance for offline mobile forms.

### Interfaces

#### Elevate multi-pane experiences by adding headers to your pane layouts

We know you love to use the recently released pane layout with up to three independently scrollable areas. So now, we're supporting pane layouts within header content layouts -giving you the flexibility to add UI elements such as title bars and secondary navigation controls that can span all panes. Whether you're building data dashboards or lists with filters, combining pane and header content layouts gives you more power to meet diverse user needs.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

#### Add links to tag items

Tags are a great way to highlight information in your interfaces. In this release, we've made tags more flexible by adding support for all link types. Just use the new link parameter to easily apply any link type you want to a tag—including record links, report links, safe links, document download links, and more. With this enhancement, it's easier than ever to create dynamic, intuitive interfaces.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

#### Design interfaces even faster

This release, Design mode in the interface object is now up to 20% faster—enabling you to make your ideas a reality quicker than ever.

### Mobile

#### Optimized performance for offline form re-evaluations

We've continued optimizing the offline mobile experience with improved performance for offline form re-evaluations. These improvements will lead to faster evaluation times and a better overall user experience.

## Administration

Each release, we continue to give administrators more control over how they manage, secure, and administer their Appian applications. This release, we've improved your authentication experience, with new authentication methods for connected systems and improved security on some existing authentication methods.

### Entra ID authentication for SharePoint connected systems

We're committed to keeping your applications compatible with important external services like your SharePoint instance. Since Microsoft is retiring Azure ACS authentication , you can now update your SharePoint connected system objects to use the Entra ID authentication type. Once you have your credentials, you can quickly update the connected system in Designer.

### OpenID Connect authentication for HTTP connected systems

Keeping with the authentication theme, we are also expanding your ability to use OpenID Connect for  single sign-on with Appian. Now, with just a few clicks , your HTTP connected systems can call integrations on your users' behalf using the OIDC user authentication setup configured by your administrator. Since users will no longer need to manually sign in to external services, you can build frictionless workflows that keep users focused on the task at hand.

### Protecting systems by rate limiting multi-factor authentication requests

To improve sign-in performance and security, we're now limiting the number of times a user can request a new verification code. After three code requests, the user won't be able to make additional requests for 15 minutes.

### Upgrade search server to version 8

This release, we've upgraded the Elasticsearch server from 7.17 to 8.14 and introduced a new search server authentication mechanism. This means that self-managed customers will now need to provide a password in the configuration file, instead of an API key .

## Behavior changes

This section describes behavior changes in Appian 24.3 that impact how you previously used or interacted with an existing feature, functionality, or the platform in an earlier version. This includes any changes that require you to modify your application after upgrading to Appian 24.3.

### Pane layouts in header content layouts

In Appian 24.2 and 24.1, a workaround inadvertently allowed pane layouts to be displayed in the same interface as header content layouts. Now that pane layouts are supported with header content layouts, this workaround will no longer work in Appian 24.3. Before upgrading to 24.3 make sure you are not using a pane layout with a header content layout in an existing interface, or the interface will break on upgrade.

## Resolved general issues

- AN-275116 - High Resolved a rare occurrence where record actions would fail to generate on certain record types backed by PostgreSQL tables.

- AN-237448 - High Fixed an issue in which long-running syncs that fail to complete prevent a new sync attempt from initiating.

- AN-277962 - High Fixed an issue that led to slower syncs for a few data sources when handling NULL fields.

- AN-276666 - High Resolved an issue where phpMyAdmin activities were not considered in the idle session timeout. With this fix, users will no longer experience frequent logouts due to short idle session timeout settings while actively working in phpMyAdmin.

- AN-262536 - High Fixed an issue which allowed multiple sync executions to occur on the same record type at the same time risking a sync error.

- AN-278225 - Medium Fixed Export to Excel to support new Date with Timezone and Time with Timezone data types.

- AN-278232 - Medium Fixed an issue where the "Save Into" variable of a CDT was not showing.

- AN-276174 - Medium Fixed an issue where previewing an interface in different locales did not update values in translation string variables

- AN-229408 - Medium Fixed an issue where < and > characters were being removed in a rule input description.

- AN-271494 - Medium Fixed an issue in the Write Records smart service where a permission issue on a related record type prevented a user from writing to the base record type, even when the related record type was not referenced.

- AN-272330 - Medium Upgraded Commons Compress Library for security fix.

- AN-271014 - Medium Fixed an issue when trying to force log out users prevented the user session from being logged out.

- AN-275211 - Medium Improved performance of loading record views by eliminating some extra queries.

- AN-275908 - Medium Fixed an issue where page width was sometimes not respected in embedded interfaces

- AN-281429 - Medium Fixed an issue where completing a record action in an interface showed an error.

- AN-270730 - Low Fixed issue in selection grids where selecting an action from a row also selected the row.

- AN-263738 - Low Fixed an issue where after updating the write record smart service to write to a different record type it displayed the event history of the previous record type as a precedent.

- AN-268635 - Low Fixed an issue to provide more information with an error code to better assist with troubleshooting for service-backed record types.

- AN-276793 - Low Fixed an issue where queries with a!queryRecordType() had intermittent errors with the error code APNX-1-4198-000.

- AN-278313 - Low Fixed issue where a relationship created using custom record fields as the common field showed as invalid in the Modify Source Fields dialog in a record type.

### Resolved accessibility issues

- AN-253146 - Critical Fixed an issue where the JAWS screen reader was not announcing system error messages when they become visible.

- AN-275451 - High Fixed an issue where instructions for radio button groups were associated with each radio button instead of the radio button group label.

- AN-263627 - Medium Fixed an issue where semantic list markup was not being interpreted by screen readers in the milestone component.

- AN-275209 - Medium Fixed an issue where non-sighted users were not notified of the successful result of saving their user filters.

- AN-275448 - Medium Fixed an issue where instructions provided for the card choice component were not programmatically associated with the component group label.

- AN-244538 - Low Fixed an issue where screen readers were not interpreting the date picker as an application and added specific instructions for screen reader navigation within the picker to accommodate for support-level variations of Windows screen readers.

- AN-277330 - Low Fixed an issue where help tooltips for radio button groups were included in the radio button group label.

- AN-267269 - Low Fixed an issue where help tooltips for radio button groups were associated with each radio button.

- AN-227499 - Low Fixed an issue where the group label for cards in the card choice component was being announced by screen readers as each card received keyboard focus.

- AN-204234 - Low Fixed an issue where the aria-describedby attribute was set to an incorrect value when instructions or a help tooltip are not provided for the card choice component.

## Evolutions

The following functions, components, or smart services have newer, improved versions in this release. Existing, old versions in your applications will continue to function normally, but will be renamed on upgrade to indicate that they are older versions. As always, make sure you are using the right version of the docs for your version of Appian. See Function and Component Versions for more information.

### a!tagItem()

The tag item component was evolved to allow you to add any link type to a tag .

## Deprecations

The features listed below are deprecated and will be removed in a future release of Appian. Do not begin using deprecated features, and transition away from any prior usage of now deprecated features. Where applicable, supported alternatives are described for each deprecation.

### Upcoming end-of-support for older versions of RDBMS

The following relational database management systems (RDBMS) either have already reached or are approaching the standard end-of-support dates set by their vendors and will no longer be supported in a future release of Appian. Customers are strongly advised to upgrade to a newer supported version .

### RHEL and CentOS versions

The following operating system versions are no longer supported starting from 24.3 and in all future versions. Self-managed customers are strongly advised to upgrade to a newer supported version .

## Removals

The features listed below have been removed from Appian and can no longer be used.

### End-of-support for older versions of RDBMS

The following relational database management systems (RDBMS) have already reached the standard end-of-support dates set by their vendors and are no longer supported in Appian.

### Forms Designer and non-SAIL forms in Appian Mobile

The Forms Designer has been removed from Appian; it was deprecated in Appian 16.3. You will no longer be able to access the Forms Designer to edit non-SAIL forms, though existing non-SAIL forms will continue to work.

Additionally, as of June 21, 2024 users are no longer be able to access non-SAIL forms in the Appian Mobile app; this capability was deprecated in Appian 24.2 . Users can still access them using a browser.

If you are using non-SAIL forms and want to edit them or access them through the Appian Mobile app, convert them to interface objects .

## Feedback


---

## Appian 24.4 — synced 2026-08-16

Source: https://docs.appian.com/suite/help/24.4/Appian_Release_Notes.html

# Appian Release Notes

Share via

LinkedIn

Reddit

Email

Copy Link

Print

24.4 Release Highlights

Join our Appian Community team and other Appian experts as they dig into highlights from the 24.4 release.

Join our Appian Community team and other Appian experts as they dig into highlights from the 24.4 release.

## Release Highlights

This release introduces many new and exciting features throughout the platform that make it faster to understand, interact with, and explore data across your applications. We're particularly excited to shine a spotlight on two standout features this release: process autoscaling and FedRAMP certification for many of Appian's AI capabilities.

### Introducing process autoscaling

Process automation is key to the efficiency of your business, helping you to complete critical work faster and with greater precision. Now, Appian is making your automation journey even better by introducing autoscale for your processes.

Autoscale is specifically designed to orchestrate complex workflows that experience high volumes and require high throughput. This capability makes it much easier to tackle the volume of automated loan approvals, securities monitoring, and other volume-intensive use cases. If demand spikes, processing capacity increases automatically to accommodate usage, ensuring business continuity without disruption or having to pre-provision resources.

You can easily autoscale your new or existing processes, and leverage a subset of familiar nodes and smart services to quickly build your automated processes.

#### Monitoring autoscaled processes

Once your autoscaled process is up and running, you can use a brand-new set of monitoring tools to see how your process is performing. These tools are designed to let you observe millions of process instances at a glance by aggregating the most important data about your processes.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

If there is a spike in errors, you can take action and dig into individual process instances to look into any issues using process history optimized for autoscaling mode.

### Multiple AI features achieve FedRAMP Moderate compliance

We're excited to announce the expansion of FedRAMP controls across most of Appian's AI capabilities. Now, in addition to document classification, document extraction, and email classification, all AI Skills and most AI Copilot features are FedRAMP compliant. These features meet the stringent security, privacy, and operational requirements for public sector use, enabling more government agencies to automate complex processes with confidence.

Stay tuned for further updates about Appian's security and compliance certifications.

### Preparing for containerized self-managed Appian in 2025

We understand that your deployment type directly impacts how you manage and use Appian. That's why we're sharing the details about an important change for self-managed deployments well in advance.

Starting with Appian 25.4, all new versions of Appian will require containers managed by Kubernetes to run in a self-managed environment. You won't be able to obtain Windows or Linux installers for Appian for 25.4 and its hotfixes.

Appian 25.3 will be the last supported non-containerized version and supported with hotfixes and critical updates for its full support period .

Appian runs on containers via Kubernetes , an industry-standard container orchestration platform. Appian has been running Appian Cloud on containers for several years, and most Appian Cloud sites are running on a Kubernetes based infrastructure already. Running Appian on containers has a number of benefits compared to Windows or Linux server deployments, including:

- Installing, configuring, and upgrading Appian is faster and simpler, which allows for more frequent feature and security updates with less downtime and maintenance.

- Lifecycle operations such as startup and shutdown procedures are automated to remove opportunities for human error.

- Having self-managed and Appian Cloud customers on a standard deployment infrastructure allows us to deliver new features, enhancements, scalability, and reliability improvements to you more rapidly.

To provide you with a variety of options, Appian runs on OpenShift, Azure AKS, Amazon EKS, Google GKE, or your local or collocated "bare metal" Kubernetes cluster.

To help you with this transition, visit our migration toolkit . If you are interested in migrating to Appian Cloud, where you would no longer be responsible for managing your Appian instances or supporting infrastructure, reach out to your account executive for more information.

## Appian AI Copilot for business users

Through these features, AI Copilot helps business users be more productive and have an easier time working with applications.

### Better conversations with Enterprise Copilot

Experience more natural and engaging conversations with Enterprise Copilot through advanced language understanding and improved response quality. Now, it's easier than ever to communicate naturally with your knowledge sets.

### New regions for AI Copilot for reports, records chat component, and Enterprise Copilot

This release expands the regional availability of AI Copilot for reports and the Records chat component to include the following regions:

- Asia Pacific (Mumbai) ap-south-1

- Asia Pacific (Seoul) ap-northeast-2

- Asia Pacific (Singapore) ap-southeast-1

- Asia Pacific (Sydney) ap-southeast-2

- Asia Pacific (Tokyo) ap-northeast-1

- Canada (Central) ca-central-1

- Europe (Ireland) eu-west-1

- Europe (London) eu-west-2

- Europe (Paris) eu-west-3

- South America (Sao Paulo) sa-east-1

This release also expands the regional availability of Enterprise Copilot to include the following regions:

- Asia Pacific (Mumbai) ap-south-1

- Asia Pacific (Singapore) ap-southeast-1

- Asia Pacific (Sydney) ap-southeast-2

- Asia Pacific (Tokyo) ap-northeast-1

- Canada (Central) ca-central-1

- Europe (Ireland) eu-west-1

- Europe (London) eu-west-2

- Europe (Paris) eu-west-3

- South America (Sao Paulo) sa-east-1

For a complete list of supported regions, see Security and Compliance .

### Experience the full release of AI Copilot for data fabric

Previously available as a preview, we are excited to announce the full release of AI Copilot for data fabric , featuring faster response times and a better overall experience. You'll notice up to 40% faster responses, making your interactions with AI Copilot more efficient. Plus, while you wait for answers, you'll now see real-time progress updates through new chatbot messages, ensuring a more transparent and engaging experience. Additionally, AI Copilot now supports up to 250 record types in the data catalog, up from 60, allowing you to leverage even more data for deeper insights.

These updates provide an even better experience and mark the general release of AI Copilot for data fabric.

## Appian AI Copilot for developers

AI Copilot also helps developers be more productive and have an easier time building applications.

We're excited to share an update that makes it easier for developers to build interfaces.

### PDF-to-interface now powered by Appian's private AI

Generating an interface from a PDF is now powered by Appian's private AI . This enhancement simplifies your toolset by eliminating the need for an external Azure OpenAI license. Enjoy the efficiency AI Copilot provides while your data remains secure, as always, within Appian's private AI framework. Additionally, this feature is included in the batch to receive FedRAMP compliance , announced above.

For cloud customers in regions not supported by private AI, access to this capability may be limited unless cross-region configuration is enabled.

With this release, self-managed customers will no longer have access to the PDF-to-interface capability. If this capability remains active, it may cause errors. To prevent issues, we recommend removing OpenAI credentials to disable and hide this capability when building interfaces.

## AI Skills

AI skills enable you to build, configure, and train a custom machine learning (ML) model to use in your processes. This release, we've made it simpler to extract data from tables that span multiple pages in your documents.

### Effortlessly extract data from multi-page tables

The document extraction AI skill can now automatically detect and extract tables that span multiple pages within a document. This means you no longer need to use complex workarounds to merge multi-page tables. During the reconciliation task, Appian will seamlessly consolidate them into a single table field, saving you time and effort. Once you've completed the reconciliation step , future table extractions will happen automatically—helping you work faster.

### See beyond text and unlock data from visuals

Previously limited to text-only data, you can now use generative AI skills to extract insights from visual data within your documents such as checkboxes, charts, images, and other visual content. Our enhanced visual extraction capabilities allow you to automate more work and unlock deeper insights from your documents.

## RPA

### Stay secure and efficient with automatic RPA autologin updates

The RPA autologin service now automatically updates to the latest version when connecting to a newer version of Appian RPA. You’ll always have the most up-to-date security features and performance enhancements, reducing the need for manual updates and minimizing downtime. With this update, you can focus more on your work while the system takes care of staying current and secure.

Tip: A warning icon will display next to your robot until the robot is updated with the latest autologin service.

## Process HQ

Combining the latest technologies in data fabric, process mining, machine learning, and generative AI, Process HQ gives business users the power to explore data and identify timely insights they can use to optimize their business. We've added new enhancements to both of Process HQ's key capabilities: process insights and data fabric insights .

### Process Insights

Process insights fulfills Appian's promise to eliminate the complexity and subjectivity of process analysis and make it objective, accurate, and easy. This release, we've made it even easier to identify and eliminate bad process outcomes, create KPIs using AI Copilot, and explore more aspects of your processes.

#### Reduce bad process outcomes

The best indicator of potential process improvement isn't always how long a process takes. It can also be how often something happens during that process, usually something bad. This release, we're letting you investigate exactly that—how often parts of your process or cases with certain attributes occur—so you can quickly reduce those occurrences and get the most out of your processes.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

While focusing on the occurrence of characteristics, activities, or sequences in your process, you'll be able to drill down on additional characteristics the same way you would with long durations. And, each step of the way, Process HQ will clearly report how many occurrences you can eliminate to see real improvement in your KPI.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

With this new way of looking at process data, you'll get a fresh perspective on how much better your process can be.

#### Create KPIs and act on insights faster using AI Copilot

Last release, we introduced AI Copilot into process insights to help you create views faster and more easily using AI. This release continues on that theme, now for KPIs and insight summaries!

AI Copilot makes it easier to create KPIs specific to your business by analyzing your process data and generating suggested measurements. When you select an AI-generated KPI, you're able to edit all of the suggested configurations to fit your needs.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

We're also making it easier for you to draft useful summaries and recommendations within insights , so you can boost the speed of collaboration across your organization. AI Copilot provides you with starting text based on insight details and business best practices. Edit the AI-generated draft, or regenerate content until you're happy with what's being communicated.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

Wherever you use AI Copilot in process insights, you'll notice that AI-generated suggestions persist between sessions and users. This means that if you generate suggested KPIs using AI Copilot, you and your collaborators will see the same suggestions. This small change is just one more way we're making it easier and faster for you and your teams to explore a process.

#### Explore case attributes with ease

This release, expanded case attribute data in process views makes it even easier to understand your complex process data. In the new case attributes grid, you can quickly review key metrics for various attributes and compare values across attributes and within a single attribute. Plus, with new search and filter capabilities, you can hone in on specific attributes to review and compare.

When you're ready for a closer look at an individual attribute value, an enhanced Attribute Details dialog is just one click away.

Here, you can see the potential savings for cases with the attribute value. Distribution and trend visualizations, as well as a case list, help you easily contextualize the attribute and validate what you're seeing.

Then, to add more process characteristics to your analysis, you can start an investigation directly from the dialog. With your attribute data right where you need it, the journey from discovery to diagnosis is faster than ever.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

#### Access activity details directly from the process diagram

In process insights, the process diagram gives you a unique picture of where and when activities happen in your process. Now, you can move seamlessly from understanding activities in that context to drilling deeper on an individual activity.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

Simply click an activity node in the diagram to view findings, potential savings, and visualizations for that activity. Then, once you've decided to look closer, you can start an investigation right away.

#### Collaborate even faster with direct links to your investigations

This release, you can share a direct link to an investigation that jumps immediately to the investigation details . Help your collaborators and stakeholders get right to the insights they need with even fewer clicks.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

#### Get better insights with smarter process filters

This release, we've added enhancements to help data stewards easily optimize business data for analysis in process insights.

Once your data is in process insights, AI Copilot will automatically detect ad hoc events and even suggest filters to remove them from your process data, so it's even easier to focus on the activities that matter most.

With better business data, you'll have a better picture of your overall process and uncover meaningful insights faster than ever.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

#### Improve your process data with enhanced custom attributes

Last release, we introduced the Find and Replace custom attribute template to help you optimize your data in process insights. This release, we've enhanced the template with even more options, so you have even more flexibility to find and replace values in your data.

Now, in addition to text fields, the Find and Replace template can help you find and replace values in integer and boolean fields. We're also giving you the ability to replace null values and non-null values, so you can make sure your data is meaningful, consistent, and easily readable.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

We've even added support for filtering process data based on custom attributes, giving you more control over what's included in your process data.

#### Add helpful context to attributes

Data stewards and analysts can now add attribute descriptions right in process insights to help analysts gain a better understanding of process data. And, you can now see attribute descriptions in more places across process insights, so that important business context is easier to find. With this enhancement, business analysts can easily improve their interpretation of your process data and make better decisions to optimize processes.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Data Fabric Insights

Data fabric insights empowers any user to explore their enterprise data and find answers to their common business questions. This release, we've made report filters more flexible, introduced new quick filters, and optimized reports so users can experience more performant dashboards.

#### Flexible filtering on reports

This release, we've given report creators more control over how they filter their reports by making our filters more flexible and dynamic.

Now, report creators can easily filter by a list of values. Whenever they select a text field, report creators can use the Equals and Does not equal operator to filter by one or more values. And, we'll provide users a list of values from the selected field so they can easily pick their values.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

Report creators can also dynamically filter data by the current or next day, week, month, year, or quarter. For example, instead of regularly updating a filter in a report to show data for the current week, report creators can use a dynamic filter operator to automatically get this data. We'll even show the dates for the selected time frame so report creators can be confident that they're filtering by the right dates.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

#### Allow any user to filter a report

Report creators can also add new quick filters on any report by simply selecting a field. With just a click, report creators can display a list of filter options directly on the report, allowing any report viewer to filter the data to best fit their needs.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

#### Expanded list of chart options

We've also restyled the Design palette so users can now select donut, stacked, and 100% stacked chart options directly from the palette—allowing users to jump-start their designs with minimal configuration. Users will also notice a few small but mighty design enhancements that make it quick and easy to configure different aspects of their reports.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

#### Load KPIs asynchronous

Last release, we improved the performance of dashboards containing large or complex grids by asynchronously loading grid data in the background. This release, we're also loading KPI reports asynchronously, so users will notice overall more performant dashboards—especially those containing grids and KPIs.

## Data Fabric

Appian's data fabric stitches together data from multiple systems into a single, secure data model, so you can build applications quickly. This release, you can now inherit sync filters from related record types, provide multiple default values in your user filters, and subscribe to conversations on your records.

### Sync data based on relationships

This release, we're taking sync filters to the next level by allowing you to filter by source fields and by a relationship.

When you filter by a relationship , your record type will automatically inherit any filters applied to the related record type. For example, the Project record type has a sync filter configured to only sync active projects. Since the Task and Project record types are related, you can filter by that relationship to only sync tasks for active projects.

You can even filter by the related record fields from the selected relationship to make your filter more precise. For example, you could also filter by the project year so you only sync tasks for active projects in 2024.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Provide multiple default options in user filters

We're excited to share that you can now provide multiple default options in your user filters . This way, you can automatically filter your record lists and records-powered grids to show users the exact data they need.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Automatically recover failed smart service syncs

We know that reliable, up-to-date data is vital to any application. That's why we're introducing a new sync option to automatically recover your data when a sync triggered by a smart service fails.

When the Recover smart service syncs option is enabled, a recovery sync will kick off immediately after a failed smart service sync—no manual intervention required. Recovery syncs will fetch and re-sync all of your source data to ensure you have the latest changes as quickly as possible.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Create synced record types from large data sources

The Keep data available at high volumes is a powerful sync option that ensures your data is always available when you need it. This release, you can now enable this option during initial set up so you can connect your record types to even larger data sources.

When enabled, Appian will automatically sync the latest 4 million rows in your record type so you can immediately start working with that data in Appian. To ensure the latest data is synced at least once a day, we'll automatically schedule full syncs , which you can edit at any time.

By enabling these sync options up front, you can easily access more of your enterprise data in Appian, and be confident that you're working with the latest data.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Subscribe to conversations on records

With record events , you can enable collaboration on your record types so users can have conversations and ask questions directly in the context of their records. Now, it's even easier to stay in the loop and keep conversations going by subscribing to conversations about a record. When you subscribe to conversations, you'll receive an email notification any time someone adds a new comment or reply to a conversation.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

When users subscribe to conversations, Appian automatically stores the subscribed user in a new Subscriber record type. You can generate this new record type when you first configure record events, or you can easily create a new record type to store subscribers and update your existing record events configuration.

### Quickly configure security rules by copying existing rules

We've made it faster to configure record-level security by allowing you to duplicate existing security rules . Now, with just a click, you can get a jump-start on your security configurations.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Easily view record type source information

This release, the record type will now display all of your important source information at a glance. In addition to the source type and table name, the record type now displays the name of the data source—giving you quick insight into where your data is coming from.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Query record data faster with rv!record

This release, we've enhanced rv!record so it can automatically detect if fields have already been queried from a different relationship and skip any redundant fields—optimizing your record views and titles so they only query the data you need.

To take advantage of this enhancement, simply update the record type .

### Simplified field selection in service-backed record types

Service-backed record types make it easy to connect to data in any external system, and this release, we've made it easier to map fields from your external system to fields in the record type.

Now, Appian will automatically suggest all top-level fields returned by an integration as fields in the record type—even fields with null or empty values. With this enhancement, it's now faster and easier to access the data you need.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Updated configuration experience for data stores

We've updated the data store object to have a more modern look and feel. Now, when you create or edit a data store object, you'll see a refreshed interface that's more intuitive to use.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### New Enhanced Data Pipeline (EDP) Credentials API

This release, we're introducing a new Cloud Database Management REST API that makes it easier to update the user credential for Enhanced Data Pipeline (EDP). The update EDP credential API endpoint allows you to integrate with a privileged access management system and update EDP user credentials programmatically. This new API will simplify your password change process and help meet security requirements for privileged cloud database access.

### Allow a list of values in a SQL Integration query parameter

When used together, the custom JDBC connected system and the SQL integration object let you easily use SQL statements to connect your Appian apps to an unsupported database and exchange data. This release, we've made it even easier. Now, simply pass a list of values into each parameter in the SQL integration directly, and use the IN operator in your query filter. No further configuration required!

### More connection property configurations for data source connected systems

This release, we've provided an option to add more connection properties for your data source connected system to streamline the configuration experience. Now you can configure the additional properties directly in the connected system—no need to rely on the connection URL or pause your work to open a support case.

### Upgraded JDBC driver for MySQL

The default JDBC driver for MySQL has been upgraded from version 5.1 to 8.4.

In 8.4, the nullCatalogMeansCurrent connection property now has a new default of false .

To maintain backward compatibility and ensure a seamless upgrade experience, we'll automatically set nullCatalogMeansCurrent=true for you, unless you've already configured it yourself—no manual adjustments needed.

## Case Management Studio

This release, we're continuing to improve Case Management Studio to best fit your case process needs with enhancements to case routing, workflow automations, and case creation flows.

### Improve your workflow efficiency with automations and case routing

We're helping you refine and automate workflows with enhancements to the Automated Case Routing Module and the introduction of automations to workflows.

Now, in just a few clicks case managers can create rules that automate case assignments based on case type, case category, and case fields, as well as reference custom case fields configured in Studio—no extra steps necessary!

And, new workflow automations can help you to extend your automation capabilities within Studio. Automations allow you to easily define rules and criteria that specify how to move forward in a workflow without human intervention.

### Transform emails into cases in a snap with the Case Creation via Email module

This release, we're making case creation more flexible with the Case Creation via Email module. The triage queue in Workspace allows you to pull in emails and turn the inquiries into new cases or add information to existing cases, directly from the queue.

Once you've created or updated a case, we'll display the email thread and any new replies to the thread on the case itself. And, you can even reply to emails directly from within the case.

We're centralizing case information and creation, so that you can spend less time digging through emails and more time focusing on resolving cases.

## Sites and Portals

Appian enables you to create superior, seamless experiences across desktop and mobile devices for all your users using portals and sites . This release, we've made it easier to display your portal in different locales, monitor your portals usage, and display your portals in more places.

### Develop multilingual portals for a global audience with simplified localization

Localizing portal content just got easier. Starting this release, you'll be able to more easily display your portals in multiple locales, including updating translation strings, layout, and date formatting to match the locales you specify.

Using the new a!portalUrlWithLocale() function, you'll be able to create a link that allows users to switch between different locales directly in a portal. We've also added a locale parameter to the a!urlForPortal() function that you can use if you know your users' preferred locale when creating a link to the portal. The locale will even persist as users navigate to other pages in the portal.

With improved localization support, portals can seamlessly serve users everywhere.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Understand your portal users with a new usage log

With the new portals usage log , you can now gain valuable insights into how end users are interacting with your portals. Accessible from System Logs, you can use the downloadable log to view key metrics like session IDs, IP addresses, visited pages, and device information.

Now, you can see which pages are most popular or which devices users connect from, giving you a holistic view of real user behavior that will help guide your future portal strategy and development.

### Display portals anywhere in iframes

We're giving you more flexibility and control by enabling you to display portals on external websites. This seamless integration using iframes makes it possible for you to display a portal like it is a native part of your own website.

### New standard logo on sites

This release, we’re introducing a standard Appian logo on site navigation bars in certain Appian Cloud environments.

## Interfaces

Appian makes it easy to build beautiful, information-dense interfaces that you can use throughout your applications. This release, we're excited to share new, powerful components, the latest enhancements to read-only grids and KPIs, and asynchronous loading of your data-rich components.

### Create beautiful, responsive card groups

Make your information dense interfaces more organized and elegant with our new Card Group Layout . Effortlessly ensure consistency, making all your cards the same height and evenly distributed in the container in just a few clicks. We handle the sizing, alignment, and responsiveness for you, allowing for minimal configurations and maximum design potential.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Supercharged read-only grids

Read-only grids are one of the most popular interface components. This release, we're giving them a fresh new look, optimizing queries to record types, and allowing you to export any data you need.

#### Smarter queries in records-powered grids

We evolved the read-only grid so records-powered grids are smarter than ever. Now, records-powered grids can automatically detect if fields have already been queried from a different relationship and skip any redundant fields—optimizing your grids to only query the data you need.

#### Sleek and modern records-powered grids

Additionally, your automatically generated record lists and records-powered grids have improved styling and layout, optimized for both desktop and mobile.

Right out of the box, the updated record lists provide a more polished and intuitive interface. This speeds up your development and allows you to focus more on your core application functionality. And, you can use the refreshed default styling as inspiration to start modernizing existing grids throughout your apps.

You'll also notice that as a part of this release's evolution of read-only grids , the default styling for all read-only grids has a more modern look.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

#### Curate which grid columns to export to Excel

Finally, we've added a new exportWhen parameter to columns in a read-only grid so you can choose exactly which columns are exported and which aren't. You can even export additional columns that don't display in the grid, curating specific data that is only available on export.

### Display your interface while data-heavy grids, charts, and KPIs load in the background

This release, you can enable asynchronous loading on read-only grids, charts, and KPIs. This allows faster-loading components to appear immediately, while your most data-heavy grids, charts, and KPIs load in the background, ensuring users can begin interacting with key elements of the interface right away.

We'll even display a loading indicator to ensure users know the data is on the way. By reducing the initial wait time, users experience a more responsive interface, keeping them engaged and productive.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Take complete design control of your headings

Introducing the heading component ! The headings component is a new way to intuitively structure and easily organize your interface with both visual and non-visual indicators to help all users quickly understand your content.

This component gives you more heading configuration options, so that you can have complete control over the color, size, and font weight for each heading. And, you can set accessibility heading tags to make your interfaces more accessible to screen-reader users.

The heading component provides a more intuitive and flexible design experience for developers, while simultaneously allowing you to create a more elegant and accessible experience for your users.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Empower users with more options in the styled text editor

This release, we're improving styled text editor with new formatting options and controls, available on desktop, mobile, and offline.

Now, users can format text as tables in the styled text editor , empowering them to showcase information in a clear, scannable manner. And, we've introduced a new allowedFormats parameter so that developers can precisely control which styles users can apply in the styled text editor. We've also added a new tooltip that lists all keyboard shortcuts for the editor to improve accessibility and help all users be more productive.

With these new options, you can provide even more formatting options to all of your users while allowing you to fine-tune their experience.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Make your card colors more consistent with new card border colors

This release, we're adding even more card configuration options, with the ability to choose a color for your card borders. In just a few clicks, you can set a custom or predefined card border color to easily make your UIs more visually cohesive and effortlessly match your organization's branding guidelines.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Design your interfaces with strikethrough text

We're introducing more styling options to the rich text display component with the addition of strikethrough formatting. Strikethrough formatting allows you to easily compare text revisions with a simple line through the text. Need to indicate that text is no longer relevant, accurate, or valid? No problem! With more formatting options, we're helping you create the design you want while giving your users the context they need.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Style your KPIs

With the KPI component , you can highlight vital metrics from your record data in a meaningful, easily digestible display. This release, we've added a new parameter allowing you to apply text formatting to the primary text to give your KPIs a consistent appearance and help them stand out on your interfaces.

## Mobile

Appian Mobile enables users to monitor, collaborate, and take action on their applications, all from the convenience of their iOS and Android device. This release, we've made it easier to sync your offline data, design offline mobile forms, and resiliently recover data.

### Simply sync your offline data in one tap

We're introducing a simple method for users to sync their offline actions and tasks for offline use. The new Data Sync option in the Appian Mobile menu allows offline users to sync all offline data from a single convenient location. And, with just a quick glance at the mobile menu, users can see the exact date and time that their data was last refreshed.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Design offline forms using record data types

Now you can extend your data fabric to offline forms by using record type references to query record types . This means you no longer have to rely on custom data types (CDTs) when building offline forms, unlocking greater flexibility and power. For more information about what record features are and are not supported in offline interfaces, see Offline Mobile Design Best Practices .

### Automatically recover data in offline actions

We're helping safeguard user-entered data and minimize risk of data loss with automatic recovery for offline actions. When a form that closes unexpectedly is reopened, we will now auto-populate the form with the previous data so users can pick up right where they left off. Users can complete offline actions with confidence, knowing their data will be persisted.

## Expressions

Expressions make it quick and easy to access the data you need throughout your applications. This release, you can test those expressions more quickly with new default test cases.

### Quickly test expression rules with default test cases

We've made it easier to test your expression rules in a number of ways.

You can now set a default test case, and we'll automatically load it whenever you open an expression rule for testing.

You can quickly switch between test cases with a new dropdown menu, making your expression rule testing faster and better than ever.

And, you can also change the output of a test case from formatted, to raw or expression, in one click. Now your test outputs require no additional reformatting.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

With faster and easier testing, we're helping you increase developer productivity and create overall more robust applications.

## Deployment

Appian is dedicated to providing you with an efficient and enjoyable deployment experience that fits seamlessly into your DevOps pipeline . This release, you'll appreciate enhanced deployment security.

### Enhance your deployment security

We know that the security of your environment is a top priority, so this release, we've enhanced our deployment review process. Now, to support your auditing and security requirements, you can prevent the same individual from requesting and approving the same direct deployment.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

## Administration

Each release, we continue to give administrators more control over how they manage, secure, and administer their Appian applications.

### Secure inbound API transactions with mutual TLS

With a wide range of security compliance certifications, Appian makes it easy to build applications that meet your organization's data protection and security requirements. This release, we are enhancing security for system-to-system communication by letting administrators configure mutual TLS (mTLS) authentication for an environment's web APIs. For complete instructions on enabling mTLS in the Admin Console, see the Web API Authentication page.

### Control Process HQ's AI capabilities in one click

We've made it easier for administrators to control the availability of generative AI features in Process HQ . Now, you can choose to enable or disable AI Copilot in Process HQ from the Admin Console . The setting applies to AI Copilot for data fabric, AI Copilot for reports, and AI-generated suggestions for views, KPIs, and insight summaries.

### Stream Tomcat access logs in Appian Cloud

Tomcat access logs offer essential data for application monitoring, user behavior analysis, and various operational needs. With this release, you can now stream the Tomcat access log for enhanced, real-time insights and monitoring capabilities. This real-time security monitoring in Appian makes it easier for you to meet the compliance and auditing requirements of your industry.

### Enforce file extension blocking for compressed files

We've enhanced file upload restrictions to include the content inspection within compressed or zipped files. With the new Apply above settings to contents of compressed files , you can prevents users from bypassing file type blocks by uploading compressed versions of restricted files.

### Use self-signed certificates for TLS connections to a database

Enabling TLS encrypted connections to a database with server identity verification ensures that data transmitted between Appian and your database server is protected from interception and tampering. This release, we're enabling you to use self-signed certificates (internal or private certificates) for TLS encrypted connections to the supported databases . Just add your certificates as trusted server certificates in the Admin Console and they will be applied to database server authentication.

## Resolved General Issues

- AN-281311 - High Improved service stability

- AN-245400 - Medium Fixed an issue with the process model not loading when a banner in the Process Modeler is formatted incorrectly.

- AN-278629 - Medium Improved service stability

- AN-287356 - Medium Upgraded the Jackson core library default values for nesting depth, number length and string length.

- AN-255603 - Medium Fixed an issue with Appian integrations not timing out in cases they should.

- AN-251754 - Medium Fixed a memory leak when using HTTP Integration connected system.

- AN-280541 - Medium Improved error handling and enhanced user experience for cases where the primary measure has null values.

- AN-282146 - Medium Resolved an issue that prevented users with membership in a large number of Groups from being able to successfully interact with AI Skill objects.

- AN-287643 - Medium Fixed an internal issue that caused type errors in synchronous subprocess nodes.

- AN-285675 - Medium Improved error handling for webapp.

- AN-290183 - Medium Fixed an issue where selecting multiple users in the last modified picker in the process HQ home page showed an error.

- AN-247373 - Low Fixed an issue with connector arrow alignment when a banner is present in the Process Modeler.

- AN-264381 - Low The kebab menu now aligns with the settings defined for the component in the mobile app.

- AN-290499 - Low Fixed a bug that prevented component plug-ins from requesting geolocation, microphone, and camera permissions when used in a page of a portal.

- AN-232237 - Low Fixed an issue, where in some instance upgrading a plugin could cause the Admin Console Plugin Page to not load.

- AN-280994 - Low Fixed an issue where the signature component was not saving a provided signature on Android using a mobile browser.

- AN-285924 - Low Fixed an issue where embedded interfaces that used the styled text editor sometimes crashed.

- AN-284727 - Low Fixed a bug where the header line for logout-audit.csv was repeated incorrectly.

## Resolved Accessibility Issues

- AN-287284 - Critical Fixed an issue where the dynamic character counter value in paragraph, text, and styled text editor fields was not announced by screen readers.

- AN-279277 - High Fixed an issue where items in record action menus were not announced by screen readers as they were navigated to.

- AN-279257 - High Fixed an issue where activating a record action button caused a screen reader to begin reading at the beginning of the interface when securityOnDemand was enabled.

- AN-275098 - Medium Added a visual confirmation message that is also announced by screen readers when a user profile photo is uploaded.

- AN-285712 - Low Fixed an issue where there was no text alternative for a saved signature image within the signature component.

- AN-292718 - Low Improved the accessibility of collapsible section and box layouts by utilizing the aria-controls attribute.

### Improved accessibility in Process Insights

We're committed to making the Appian platform accessible to all users. In this release, we've made a number of updates to process insights within Process HQ to support this, including:

- We've refactored some code to make it easier for users to interact with process insights when using a screen reader or keyboard. Affected areas include field focus, navigation elements, and page structure (such as headers and lists).

- We've also updated images and icons to include descriptive alternative text and tooltips, and applied more labels to make it easier for users to use assistive technologies.

- We've updated the product to preserve navigation and interactive elements when the screen resolution is changed or zoomed in.

- We've updated multiple elements to provide sufficient color contrast so text is easier to read. We've also updated areas of the product where color was used to convey information, so relevant text provides meaning as well.

## Evolutions

The following functions, components, or smart services have newer, improved versions in this release. Existing, old versions in your applications will continue to function normally, but will be renamed on upgrade to indicate that they are older versions. As always, make sure you are using the right version of the docs for your version of Appian. See Function and Component Versions for more information.

### Unlock new modular process designs with the Start Process smart service

Rendering your complex workflows as process models is now even easier with the updated Start Process smart service . We've enhanced the Setup tab to make it easier to configure inputs and outputs, as well as added the ability to start a process synchronously.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

To support synchronous processes, we've also updated the a!startProcess() function with two new parameters.

To build interfaces that update seamlessly after an unattended process completes, set isSynchronous to true . Then, define the behavior for the onIncomplete parameter with the behavior you want if the process does not complete successfully or in the allowed time.

### Read-only grid

We've evolved the read-only grid component to enable smarter queries in records-powered grids . We've also updated the styling so grids display with light borders and no row shading by default—giving grids a sleek, modern look.

## Deprecations

The features listed below are deprecated and will be removed in a future release of Appian. Do not begin using deprecated features, and transition away from any prior usage of now deprecated features. Where applicable, supported alternatives are described for each deprecation.

Note: Administrators, see above for an announcement regarding the deprecation of non-containerized self-managed Appian instances.

### Rich text header

The rich text header component is deprecated. It will continue to function as normal in existing implementations, but may be removed in a coming release. Use the new heading component to take advantage of a simpler design experience with more flexible and accessible configuration options.

### Upcoming end-of-support for older versions of RDBMS

The following relational database management systems (RDBMS) either have already reached or are approaching the standard end-of-support dates set by their vendors and will no longer be supported in a future release of Appian. Customers are strongly advised to upgrade to a newer supported version .

### End of GPT-4 support for PDF to interface generation

On June 6, 2025, Microsoft will end support for GPT-4, impacting Appian versions 23.3-24.3. Self-managed customers using these versions of Appian will not be able to use the PDF to interface capability, which may result in errors if the capability remains active. To prevent issues, we recommend removing OpenAI credentials to disable and hide the capability when building interfaces.

## Removals

The features listed below have been removed from Appian and can no longer be used.

### End-of-support for older versions of RDBMS

The following relational database management systems (RDBMS) have already reached the standard end-of-support dates set by their vendors and are no longer supported in Appian.

## Feedback


---

## Appian 25.1 — synced 2026-08-16

Source: https://docs.appian.com/suite/help/25.1/Appian_Release_Notes.html

# Appian Release Notes

Share via

LinkedIn

Reddit

Email

Copy Link

Print

25.1 Release Highlights

Join our Appian Community team and other Appian experts as they dig into highlights from the 25.1 release.

Join our Appian Community team and other Appian experts as they dig into highlights from the 25.1 release.

## Release Highlights

This release introduces many new and exciting features throughout the platform that help you improve the scalability, speed, and performance of your applications.

We're particularly excited to shine a spotlight on three standout features this release, which ensure your applications reliably serve your needs now and well into the future.

### A more scalable and performant data fabric architecture

Appian is committed to providing scalable applications that grow with your business. That's why in this release we've enhanced our data fabric architecture to support greater scalability and performance throughout your applications and Process HQ.

With this improved foundation in place, you can now sync up to 10 million rows in each record type, and store unstructured data in your record fields !

Plus, you'll see overall performance and efficiency improvements in your sites and applications. During the data fabric enhancements beta program , participants experienced 5-10x faster performance for complex queries against record types with millions of rows – with some queries up to 40x faster! They also experienced up to 5x higher write throughput and a 90% reduction in storage space used.

### Process hundreds of millions of pages with AI skills

In this release, we've also enhanced our AI architecture to support greater scalability and performance throughout your applications.

Your processes can now classify or extract data from hundreds of millions of pages per year thanks to improved smart service throughput. If your applications handle massive volumes of documents, you'll benefit from fewer delays and bottlenecks in document processing. And you'll see overall performance and efficiency improvements in processing time, allowing you to process up to 75x more documents per hour.

### Add process KPIs to dashboards

This release, you can unify information from your process insights and data fabric insights into a centralized dashboard .

Now, you can simply drag and drop process KPIs onto your dashboard alongside your reports, allowing you to view all the relevant data from both process insights and data fabric insights at a glance.

And, each KPI has a link directly to your process, so you can quickly navigate right to your process or investigation.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

## Appian AI Copilot for business users

Through these features, AI Copilot helps business users be more productive and have an easier time working with applications.

### Chat with your data and documents directly in your app

Note: These features are available as a preview. Preview features are fully supported; however, they do not reflect the full functionality or performance of the feature yet.

Revolutionize the way you interact with your data and documents using the new a!dataFabricChatField() and a!documentsChatField() components. These functions let you embed AI-driven assistance directly into your applications, enabling real-time and context-aware conversations with your data and documents.

The new a!documentsChatField component is your gateway to smarter, document-driven conversations directly within your application. Engage with curated document sets, ask intelligent questions, and uncover actionable insights in real time—no environment switching needed!

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

Use the new a!dataFabricChatField component to integrate AI Copilot directly into your applications, making it easy to ask questions about your data fabric without switching environments. Whether your users want to find records that match their specific criteria or get information quickly, they'll see real-time answers right where you need them.

## Appian AI Copilot for developers

AI Copilot for developers helps developers be more productive and have an easier time building applications.

### New regions for sample data generation

This release expands the regional availability of AI Copilot for sample data generation to include the following regions:

- Asia Pacific (Mumbai) ap-south-1

- Canada (Central) ca-central-1

- Europe (Ireland) eu-west-1

- Europe (London) eu-west-2

- Europe (Paris) eu-west-3

- South America (Sao Paulo) sa-east-1

For a complete list of supported regions, see Security and Compliance .

## AI Skills

AI skills enable you to build and configure artificial intelligence (AI) models to use in your processes. This release includes improved scalability and performance, and new logging capabilities to enhance AI skill management and compliance.

### Easily monitor all AI usage

We are excited to introduce the AI audit log , designed to enhance enterprise security and accountability. This log helps you monitor and audit AI usage within your Appian environment, ensuring adherence to internal policies, industry standards, and regulatory requirements.

Administrators can also configure the audit log to capture additional details, including the inputs provided to the AI model and its response. This level of transparency empowers you to maintain control over AI usage while meeting evolving security and privacy standards.

### Expanded token limits for document processing

Generative AI Skills now extract complete data from any compatible document, no matter how large or detailed the response, with no output token limit holding them back. AI Skills will continue processing automatically until all data is extracted–no extra effort from developers required!

### New domains for AI Skill services

AI Skill services were updated to support the new ".us" domain for FedRAMP compliance. This change ensures the AI Skill services public URL remains FedRAMP compliant in Appian versions 24.2 and later.

To maintain access to these services, update your network allow list with the new AI Skill endpoints. For detailed instructions, refer to Add AI Skill endpoints to your network allow list .

## RPA

### Behind-the-scenes updates for RPA

We've made several behind-the-scenes updates to keep things running smoothly. There are no visible changes in this release, so you can continue developing as quickly and easily as always.

## Autoscale

Autoscale combines low-code design and business process automation with unmatched scalability. This release, we're excited to introduce features that make it easier to debug and monitor these processes.

### Autoscale receives compliance with multiple security frameworks

We're thrilled to announce that autoscale is now compliant with three important frameworks: FedRAMP Moderate, HIPAA, and PCI/DSS. This means autoscale meets the stringent security, privacy, and operational requirements for public sector, healthcare, and financial applications, opening the door for more applications to use this high-powered processing capability.

Stay tuned for further updates about Appian's security and compliance certifications.

### Interactive playback of your autoscaled processes

Debugging your autoscaled processes is now much easier thanks to the new step-by-step playback . This all-in-one view gives you a high-level look at the state of the process and in-depth details about each node.

With the step-by-step playback of how your process ran, it's simpler to understand and visualize how data flows through your autoscaled process.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Stay up-to-date on autoscaled process errors with email alerts and log streaming

For quick, up-to-date information about your autoscaled process errors, we're introducing email alerts to help process administrators resolve issues faster.

Since these processes are running at high scale, we send the first error alert immediately to let you respond at once. If a process model triggers multiple errors, we'll condense all of those errors into a single email, so you can see the big picture of how the model is performing while avoiding error fatigue.

And for environments with log streaming enabled, autoscaled process logs are now available.

### Kick off autoscaled processes directly from a portal

This release, you can easily leverage autoscaled processes in Appian Portals. We've enhanced our Portal Website Protections so your portals can kick off more autoscaled processes at the same time, enabling higher-scale usage.

## Process HQ

Combining the latest technologies in data fabric, process mining, machine learning, and generative AI, Process HQ gives business users the power to explore data and identify timely insights they can use to optimize their business.

This release, we've given the home page a new look and feel, made it easier to combine your process and data fabric insights into unified dashboards, streamlined investigations of your process, and more!

### Process HQ fully HITRUST certified

We're happy to announce that process insights joins data fabric insights in meeting all HITRUST requirements. HITRUST certification is a comprehensive security framework that provides a standardized and rigorous approach to managing risk and protecting sensitive information, including compliance with HIPAA.

### Refreshed home page

We've updated the Process HQ home page to provide a more focused experience and give you easy access to your reports and dashboards. Jump back into your recently opened items, or browse all reports and dashboards to quickly see how your processes are performing.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Build and share dashboards that combine data and process

Your dashboards tell an important story with your data. We've already highlighted how you can tell a more comprehensive story by adding process KPIs to your dashboards . This release, you can also tailor which individual users can see your dashboards and more easily customize each dashboard's look.

#### Enhanced sharing for reports and dashboards

We've expanded the collaborative power of reports and dashboards. Now, report creators can share their reports and dashboards with any user in Process HQ—not just the Data Fabric Report Creators —allowing you to share the value of your insights with more people.

The option to share with individual users makes it easier to focus your shared items on the right audience. And, you can allow individual users to edit your reports, so you can work together to maintain your reports and dashboards.

Lastly, we've added the ability to share from more places. In addition to sharing from the home page, you can now share a report or dashboard while you are viewing or editing it.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

#### Rearrange dashboards with highlighted drag and drop

In data fabric insights, we've made it easier to arrange your dashboard so it looks exactly the way you want. Whenever you drop in a new report or KPI, just look for the highlighted rectangles to add to any row or column in your dashboard.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

#### Asynchronous dashboard reports

Last release, we improved the performance of dashboards in data fabric insights by loading KPI reports asynchronously . Now, charts will also load asynchronously, allowing you to jump into editing or analysis while more complex parts of your dashboard take the time they need to load.

### Streamlined investigation of your processes

We've added more structure to the process insights workflow so you can move quickly from process overview to actionable conclusion. Each layer of analysis is highly visible as you bring your data into focus.

We start you off at the process page , where you can get to know your process as a whole with helpful metrics and visualizations.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

From that process overview, you can create individual views to zoom in on meaningful segments of your process. Each view has its own redesigned page that displays the same system-provided KPIs and visualizations as the process page, tailored to show just the view-specific data. Here, you'll also be able to quickly customize your focus by creating your own KPIs .

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

For any KPI you create, we'll automatically generate a new KPI page that displays system-provided metrics and visualizations, this time narrowed down to just cases related to the KPI.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

From the KPI page, you can drill down on specific characteristics of those related cases to get the most granular information about how your process operates. You can then assemble these details into an insight that lets you propose improvements to your organization.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

With this streamlined presentation, you can reliably move from getting to know your process to knowing what you need to do to improve it.

### Apply precise filters to your KPIs

You can now define your KPIs with even more precision, using a combination of multiple characteristics to examine and track your data.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Keep an eye on your KPIs with thresholds and alerts

To make it even easier to measure the health of your business processes at a glance, you can now set thresholds on duration KPIs to ensure your process is in line with your expectations.

You can also enable email alerts for threshold violations. Pick and choose which alerts come directly to your inbox, so that you can stay up-to-date with the state of your processes and be confident you'll never miss an issue.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

Plus, we've streamlined the KPI configuration steps. You can now create Duration KPIs and SLA KPIs in one place—the Duration KPI template.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Collaborate faster with AI Copilot in occurrence insights

Once you've identified insights into your process, it's time to share those insights with your colleagues. Now AI Copilot makes that even faster, letting you automatically generate summaries for insights in occurrence investigations, just like in duration investigations. Use the suggested text to quickly draft useful summaries so you can improve collaboration across your organization.

### Easily rename record types

Having record types with clear, descriptive names makes it easy for Process HQ users to understand the data they're working with. Now, data governors can edit the record type display name , which appears on a dataset in the Data Catalog and on a record type used in a process .

In just a click, data governors can provide clear display names that are useful to both business users and AI Copilot.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

## Data Fabric

Appian's data fabric stitches together data from multiple systems into a single, secure data model, so you can build applications quickly. This release, we're excited to introduce field-level security, support unstructured data in your record types, and a modernized look and feel to your record views and actions.

### Sync 10 million rows per record type

As your organization's data needs grow, we've ensured that your data fabric can grow with you by increasing the number of rows you can sync in each record type—from 4 million to 10 million rows !

### Configure field-level security

It's already easy to secure each row of enterprise data using record-level security , and now it's just as easy to secure each of your fields with field-level security .

Using a familiar low-code experience, you can determine who can see which fields in your record type. Then, we'll automatically apply that security throughout your apps and Process HQ , so users can see only the fields they need, where they need them.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

In some scenarios, a field will show null values if a user doesn't have access to it. To reduce confusion and visual clutter, you can use the a!doesUserHaveFieldAccess() function to hide fields a user doesn't have access to see.

With field-level security, you have greater control over who can see your enterprise data.

### Store unstructured data

We know that your data models often have fields that contain a lot of text, like support case descriptions or survey responses. Now, you can use our new Extra Long Text data type to store field values up to 64,000 characters.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Modernized record views and actions

With generated record views and actions , it's already quick and easy to set up the views and actions you need. Now, we're giving these generated views and actions a fresh look and feel.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

And, we've built in intuitive and quickly customizable defaults that will give you a jump start on building great user experiences. For example, we'll automatically choose the best field type for your inputs, such as using a paragraph component for longer text fields like descriptions.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Cleaner record view tabs

We've streamlined record views by automatically hiding record view tabs when there is only one view configured. This provides a cleaner interface for users, making it easier to focus on the content that matters most.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Write to multiple record types at once

Writing data just got easier! Now, you can use the Write Records smart service to create or update data in multiple record types—even if they aren't related. Just specify one or more record types to update, and we'll immediately write all of your changes in a single database transaction.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Easily configure unique fields in your data model

Now, you can configure unique fields in your service-backed record types so you can unlock additional relationships . For example, you can use a unique field on the "one-side" of a one-to-many relationship or on either side of a one-to-one relationship—connecting even more of your enterprise data.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Sync data in batches using URLs, URIs, cursors, or tokens

Web services often use different paging methods to return data, so this release, we're introducing a new way to page through and sync data from your external systems. Now, you can use the data returned from your integration to determine the next page of results. This allows you to page by dynamic values like URLs, URIs, cursors, or tokens.

You can easily get started by generating a record data source that uses the Batch by Text, URL, or URI method. This will automatically create an expression rule that uses the a!pageResponse() function to return the data you need and identify where the next page of results are located.

With this additional paging method, you can unify even more of your enterprise data in Appian.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Seamlessly remap record fields to different source fields

Today, it's easy to remap your record fields if you need to resolve a schema mismatch . Now, we're expanding these capabilities so that you can easily remap fields if you change the source of your record type. With just a click, you can map your existing fields to the fields in your new data source.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Power up custom record fields with the enhanced a!customFieldMatch()

We've enhanced the a!customFieldMatch() function so you can build custom record fields with conditional logic using as many record fields as you need.

And, you can now use custom record fields created with a!customFieldMatch() to filter data in a!measure() —allowing you to filter aggregations in your queries, grids, and charts.

## Case Management Studio

This release, we're continuing to improve Case Management Studio to best fit your case process needs with enhancements to case and task routing, powerful new task types, and numerous quality of life improvements.

### Simplify assignments for both cases and tasks

This release, we're making it even faster and easier for you to dynamically assign cases and tasks to the right people every time.

#### Case assignment

New automation rules for case assignment allow you to define conditional logic to specify which users and groups cases are initially assigned to, as well as dynamically adjust case assignment for in-progress workflows. Not only can you configure the conditional logic to assign and reassign cases based on specific events, such as when a case is created, a case is updated, or a case field is updated, but you can configure it all using our no-code design tools.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

#### Task assignment

In addition to new automation rules for case assignment, we're enhancing our existing task assignment capabilities to provide advanced configurations for conditional task assignment .

The advanced configurations give you even more granular control over your workflows by allowing you to select from multiple task assignment types. These allow you to assign tasks rotationally, to those with the most capacity, or to a shared queue for case workers to pick up as needed.

Our built in, no-code task assignment capabilities allow you to intelligently assign tasks in the way that best fits your needs using tools that require minimal effort and provide maximum results.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Create cases in workflow with the Create Case task type

Our new Create Case task type allows you to create new cases directly from a case workflow, helping you to organize work into distinct cases and create more flexible workflows.

When you create a new case using this task type, we'll go ahead and link the new case to the original for you. And both the new and original cases will automatically appear as related cases in both summary pages—no extra steps or configurations required!

### Send customizable emails with the Send Email task type

This release, we're also introducing another new task type; the Send Email task type. Not only does this task type allow you to send emails directly from a workflow, but it also allows you to create reusable, standardized email templates for those emails. And, each email can be fine-tuned with ad-hoc adjustments specific to the case for each task.

This task type combines the ease of reuse, the predictability of standardization, and the confidence that every email is personalized to the recipient every time.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Case Management Studio quality of life updates

In Case Management Studio, we're dedicated to not only providing big new features, but also improving the quality of life for developers and business users alike. This release we have three enhancements to help your cases and workflows run as smoothly as possible: recreating task instances, auto-resolving un-used activities, and more granular control over case and task SLAs.

Many common workflows require users to go back through a previous activity or step in a workflow. Now, we’ll create a new version of the task each time a user re-does it. This allows you to keep track of your historical data and improves the quality of your findings in process insights.

Not every path and activity in your workflow is going to be used every time. So, we will now automatically resolve all activities on unused paths, saving you time and manual effort.

Both case and task SLAs now have more configuration options. You can now set SLAs and their related due dates in days, hours, and minutes. And we've added a progress bar to allow you to more quickly and easily see where the case or task is in the process.

## Sites and Portals

Appian enables you to create superior, seamless experiences across desktop and mobile devices for all your users using portals and sites . This release, we've made portal publishing simpler, while also giving you new branding options and making it easier for users to share encrypted links.

### Simplified portal publishing

We've updated the portal design experience to no longer prevent your portal from publishing due to potential errors, allowing you to more easily catch and fix issues. Now, just like in sites, the published portal will update with your changes and the portal object will display helpful guidance on how to resolve any issues. With simplified portal publishing, you can be sure that your portal always reflects your latest changes.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Match your branding more closely with new options

This release we're bringing you new branding options that allow you to customize the look and feel of your sites and portals.

You can now specify the capitalization for all button labels and configure the shape of dialogs and tooltips. Because these configurations automatically apply to all interfaces in a site or portal, they will save you time while allowing you to better match your branding and design guidelines.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Shorter encrypted URL parameters

We've shortened the length of encrypted URL parameters created using a!urlForPortal and a!urlForSite , making it easier for users to share tailored links to specific information without reducing security. The shorter URL parameters will automatically apply to all newly generated links, while keeping your existing links fully functional.

### New standard logo on sites

Last release , we started implementing a standard Appian logo on site navigation bars in certain Appian Cloud environments. This release, sites in all Appian Cloud and self-managed environments will display this logo.

## Interfaces

Appian makes it easy to build beautiful, information-dense interfaces that you can use throughout your applications. This release, we're bringing you exciting improvements to grids, forms, milestones, and selection components, while also giving you a speedier experience when designing interfaces.

### Help your users stay organized with drag and drop grid row reordering

We're excited to introduce grid row reordering for editable grids . Now, your users can easily reorder tasks in workflows or prioritize to-do lists by simply clicking and dragging them to the desired position. You can easily enable this capability for your users in just a few clicks—no custom code or complex configuration required!

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Fine tune form formatting

This release, we're giving you more control over the look and feel of your forms. It's now faster and easier to fine-tune spacing above and below input components like text fields and checkboxes with new margin parameters. And, new parameters for form layout allow you to set the form width, background color, fixed header position, and divider line visibility. With these new capabilities, we're empowering you to create visually appealing and functional form experiences with even simpler expressions.

### Designing interfaces just got faster

You'll notice that interface objects now load much faster while designing—with performance improvements of up to 400%! These performance enhancements scale based on the complexity of the interface, so larger and more intricate designs will see the biggest boost in speed.

### Quickly configure more modern milestone styles

Creating milestones just got easier. You can now choose from three milestone styles, allowing you to quickly configure modern and intuitive status indicators and wizard steps.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Improved flexibility in records-powered selection components

This release, we've enhanced some of our most popular records-powered components, like dropdowns , radio buttons , and checkboxes . Now, you can format and display multiple record fields in the Choice Labels parameter to provide users with more information and help them easily differentiate between options.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

And, you can sort by the exact values in your choice labels by simply referencing choiceLabels in your sort.

## Appian Mobile

Appian Mobile enables users to monitor, collaborate, and take action on their applications, all from the convenience of their iOS and Android device. This release, we're bringing you improvements that elevate the user experience with offline tasks and simplify the design of offline custom task reports.

### Improved user experience for completed offline tasks

With the new a!submittedOfflineTaskIds() function, we're giving you the power to optimize the user experience of offline tasks. This function returns a list of task IDs for submitted offline tasks, making it simple for you to remove completed tasks from custom task reports when they are no longer needed. With this function, we're helping you to build more seamless offline user experiences to meet the evolving needs of your mobile workforce.

### Simplify your offline design with expanded support for offline site pages

Offline mobile now supports offline-enabled interfaces that are added directly as site pages. This new capability gives you more flexibility for designing read-only interfaces for offline experiences, such as custom task reports .

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

## Administration

Each release, we continue to give administrators more control over how they manage, secure, and administer their Appian environments. This release, we're excited to share streamline component plug-in deployments for self-managed customers, an upgraded Cloud Database version, and Enhanced Business Continuity available in more regions.

### Streamlined component plug-in deployment for self-managed customers

Component plug-ins can now be deployed on self-managed instances without a Developer Token or signature. This change streamlines the plug-in development process, making it faster and easier for developers to create and deploy custom UI components.

### Upgraded Cloud Database to version 10.6.18

Your Appian Cloud Database (MariaDB) has now been upgraded to version 10.6.18 by default.

### Enhanced Business Continuity available for European commercial AWS regions

Enhanced Business Continuity for Appian Cloud now supports sites in multiple European regions:

- Frankfurt

- Zurich

- Stockholm

- Milan

- Ireland

- London

- Paris

A site in one of these regions can be configured to backup to another of these regions.

## Resolved General Issues

- AN-302637 - High Fixed a rare issue that prevented the Appian Site from accessing AI Skills, Process Insights, and Portals features.

- AN-241158 - High Fixed a bug when importing a new data type version, removing the need to republish process models in order for them to use the latest version of the data type.

- AN-291308 - Medium Fixed an issue which caused 404 errors to show in the browser tools when opening a portal page.

- AN-284721 - Medium Fixed an issue where the sites metrics log was not getting populated with logs for Oracle backed environments.

- AN-303168 - Low Fixed the incorrect warning which displayed for the a!tagItem() function in the portal designer view.

- AN-299254 - Low During application server startup, the log now includes periodic output that lists which engines the application server is waiting on.

- AN-305735 - Low Fixed an issue that in rare cases could cause incorrect filter evaluation due to rounding errors for query filters comparing Decimal and Integer types.

- AN-285287 - Low Fixed an issue where secondary sort info was not provided in the results of aggregation queries for synced record types.

- AN-305737 - Low Fixed an issue that caused custom record fields calculating date differences to return incorrect results for negative differences where the start date is after the end date.

- AN-288517 - Low Fixed an issue that occasionally caused one-to-many related data to be sorted incorrectly for queries relying on default sorting behavior.

## Resolved Accessibility Issues

- AN-255823 - High Fixed an issue where the single or first option in a picker list was not announced by screen readers on initial search.

- AN-272225 - High Fixed an issue where a card choice component displaying a validation was not programmatically indicated as being invalid.

- AN-275463- Medium Improved the accessibility of field labels by removing redundant announcements of requiredness and the help tooltip text.

- AN-254937 - Medium Fixed an issue on the Forgot Password page where the instructions were not programmatically associated with the input.

- AN-208890 - Medium Improved the accessibility of grid fields by preserving focus within the paging controls, even as controls become disabled.

- AN-204763 - Low Fixed an issue on the Change Password page where errors were not being announced by screen readers and invalid form fields were not programmatically indicated as being invalid.

- AN-298597 - Low Improved the perceived color contrast of placeholder text for all input components by increasing the font weight.

- AN-294769 - Low Fixed an issue in grid fields where components that did not have accessibility text were incorrectly defined.

- AN-272213 - Low Fixed an issue where required card choice field options were incorrectly defined.

- AN-297190 - Low Fixed an issue in the User Settings dialog where toggles were not programmatically associated with their corresponding label.

- AN-274850 - Low Fixed an issue where the screen reader announcement was incorrect for picker components that were required, had no field label, and had reached the maximum number of selections.

## Evolutions

The following capabilities have a newer, improved version in this release.

### a!queryRecordType()

The a!queryRecordType() function was evolved so that the default value for fetchTotalCount parameter is now false . This parameter is no longer returned automatically in queries to synced record types. With this evolution, you'll notice faster queries when the fetchTotalCount parameter is false.

Existing, old versions of this function in your applications will continue to function normally, but will be renamed on upgrade to indicate that they are older versions. As always, make sure you are using the right version of the docs for your version of Appian. See Function and Component Versions for more information.

### Process investigations

In Process HQ, process investigations have evolved so that insights are associated with a related KPI, instead of an investigation. On upgrade, existing insights are automatically associated with appropriate KPIs and can be accessed from both the view and KPI pages. Users are now be able to drill down and create insights from these places in the workflow as well.

## Deprecations

The features listed below are deprecated and will be removed in a future release of Appian. Do not begin using deprecated features, and transition away from any prior usage of now deprecated features. Where applicable, supported alternatives are described for each deprecation.

### End-of-support for older versions of RDBMS

The following relational database management systems (RDBMS) either have already reached or are approaching the standard end-of-support dates set by their vendors and will no longer be supported in a future release of Appian. Customers are strongly advised to upgrade to a newer supported version .

## Removals

The features listed below have been removed from Appian and can no longer be used.

### End-of-support for older versions of RDBMS

The following relational database management systems (RDBMS) have already reached the standard end-of-support dates set by their vendors and are no longer supported in Appian.

## Feedback


---

## Appian 25.2 — synced 2026-08-16

Source: https://docs.appian.com/suite/help/25.2/Appian_Release_Notes.html

# Appian Release Notes

Share via

LinkedIn

Reddit

Email

Copy Link

Print

25.2 Release Highlights

Join our Appian Community team and other Appian experts as they dig into highlights from the 25.2 release.

Join our Appian Community team and other Appian experts as they dig into highlights from the 25.2 release.

## Release Highlights

This release introduces many new features to extend the capabilities of the Appian platform, helping you easily build, maintain, and grow your mission-critical applications.

We're particularly excited to shine a spotlight on the new no-code Control Panel centralized AI Document Center for streamlined intelligent document processing, Advanced Plug-ins like GridPlus and Microsoft Document Editor to extend platform capabilities, and a sleek, redesigned header you'll see throughout your app building experience.

### Introducing the Control Panel

We are excited to announce the release of a new workspace: the Control Panel! The Control Panel is an out-of-the-box, entirely no-code experience for business users that allows them to configure data and interfaces for their applications and workflows. The Control Panel builds off of and expands the Studio design experience we introduced with Case Management Studio so that even more users can leverage powerful no-code tools to create applications.

Unlike Designer, where low-code developers can build, manage, deploy, and monitor entire applications, the Control Panel is a workspace tailored specifically to business users. Here they can use 100% no-code tools to create the parts of the application that they know best given their in-depth knowledge of their use cases and processes.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

#### Build no-code forms directly in the Control Panel

The Control Panel's sleek and intuitive form builder allows for business users to easily build purpose-driven forms and interfaces without needing Appian training, using any code, or even hopping over to Designer.

In the form builder, business users can drag-and-drop fully configured data fields into their form—no code required! And it's a breeze to add data field validations, columns, headers, and rich text in just a few clicks.

Forms also work hand-in-hand with business users' ability to define their own data structures in the Control Panel, allowing them to reuse forms across cases and categories to speed up development and ensure consistency.

#### Enable business users to effortlessly organize data

The Control Panel also gives business users the power to create well-organized and effective data structures that perfectly fit their use cases. It's simple to create hierarchical data structures to not only logically organize your data by type and category, but to effortlessly create shared data fields that help reduce re-work and standardize data entry.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

#### The Control Panel behind the scenes

The Control Panel workspace is backed by our new control panel object , which allows low-code developers to easily define the configurations that business users can make in the Control Panel workspace.

This dynamic duo of the control panel object and the Control Panel workspace empowers business users to configure more of what they know best and better handle their own business processes, with less reliance on low-code developers.

Note: In 25.2, the Control panel workspace and control panel object can only be used and accessed by customers with Case Management Studio and other solutions that use these capabilities.

### Build AI-powered document processing workflows quickly and easily

Introducing AI Document Center : your one-stop-shop application for enterprise-grade intelligent document processing. Building on Appian's powerful AI skill library, AI Document Center simplifies the experience of building and testing your classification and extraction models, which can then be directly deployed in your business workflows . AI Document Center is up to the challenge of handling your business's highly complex documents with varied formatting and layouts, leading to higher classification and extraction accuracy.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

AI Document Center is based on proven customer success. One Appian customer, a large insurance company, has used AI Document Center to drive significant improvements in underwriting accuracy. Previously, underwriters manually processed thousands of underwriting documents, in many different formats and often handwritten, with 65% accuracy. But with AI Document Center, they're now able to classify documents and extract data much faster and with 95% accuracy, leading to monthly revenue growth of $400,000.

Quickly define your document types or fields to extract in one intuitive workflow, and let Appian create the underlying design objects for you. As you build extraction models, AI Copilot can give you an additional boost. Tell AI Copilot you want to extract data from resumés, and it will automatically create extraction fields such as name, address, email address, work history, certifications, and skills. As always, you can make any adjustments you need to as you continue configuring the model to meet your needs.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

Ready to test? Upload your test dataset to validate the model's performance directly in the app. See an opportunity to improve? Easily create a new version of the model and run additional test cases. Refine models until you are confident and ready to deploy to production.

AI Document Center provides accuracy metrics —from individual fields to the overall model—to show how things are working in both test scenarios and production usage.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Amplify Appian with Advanced Plug-ins

Appian plug-ins enhance and expand the capabilities of the platform. In this release, we're introducing Advanced Plug-ins , a new category of plug-ins to extend the scope of Appian functionality, integrate cutting-edge technologies, and address common business challenges.

Advanced Plug-ins are developed, managed, and maintained by Appian and are now available to install directly in the Admin Console for Cloud and on MyAppian for self-managed customers. This release includes two Advanced Plug-ins: GridPlus and Microsoft Document Editor .

#### GridPlus

The GridPlus component is a user-friendly interface for viewing and editing record data with extensive customization options, including column manipulation, sorting, and filtering. Efficiently manage data with multi-cell selection, inline record creation and deletion, and keyboard navigation.

We've also included the robust security controls and internationalization support you'd expect. To optimize data viewing, users can also drag-and-drop, freeze, and adjust columns.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

#### Microsoft Document Editor

This plug-in is available only for Cloud customers.

The Microsoft Document Editor component offers a seamless experience to view and edit Word, Excel, and PowerPoint documents stored within an Appian Knowledge Center. This robust plug-in allows users to directly edit files stored within Appian, eliminating the need for download/reupload workflows or separate document storage solutions. This component also enables multiple users to edit Office documents concurrently.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

Stay tuned to learn more about additional capabilities we launch as part of this offering!

Learn more about our approach to building and maintaining Advanced Plug-ins , including details about support.

### Redesigned headers deliver a more polished app-building experience

We've updated the look of the header across Appian to deliver a more modern experience for our users. The sleek new gradient design provides a fresh aesthetic that elevates Appian Designer and the Admin Console .

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

Building on these header enhancements, the interface object is also getting a modern makeover this release. In addition to incorporating the same polished gradient design, we've also updated the icons and streamlined the layout of the header. This visual upgrade helps highlight the powerful capabilities of interface objects while also making it more intuitive to navigate.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

## Appian AI Copilot for business users

Through these features, AI Copilot helps business users be more productive and have an easier time working with applications.

### Find what you need faster with smart search for record types

Note: This feature is available as a preview. Preview features are fully supported; however, they do not reflect the full functionality or performance of the feature yet.

Smart search transforms how you find records by uncovering connections, detecting patterns, and surfacing related cases across your data fabric. You can search across your entire data fabric, including text fields or documents attached to a record—all at enterprise scale. It goes beyond keyword matching by using AI-powered semantic search to understand your intent and return better results from your business data and the documents attached to your data.

For example, if you search for "electricity outage," smart search might also show results that mention "power failure" or "electricity is down." When combined with filters, smart search makes it easier to uncover connections, detect patterns, and find the information that truly matters to you.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

## AI Agents

AI agents empower you to automate dynamic and open-ended tasks within your business processes. AI skills are design objects that enable you to build and configure artificial intelligence (AI) agents to use in your processes.

This release introduces advanced document processing capabilities, high availability for generative AI, and autoscaling support—helping you tackle complexity, boost resilience, and keep performance high.

### New AI Skill to tackle your complex documents: Advanced IDP Tools

Appian is ready to help you tackle your most complex document processing challenges, with our new AI skill: Advanced IDP Tools .

Advanced IDP Tools lets developers tap into additional intelligent document processing capabilities above and beyond other AI skills. For example, it can be tricky to extract data from lengthy and complex intake forms with tables that span multiple pages, contain nested tables, or other complicated formatting.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

When called in a process, Advanced IDP Tools returns a wealth of data that wasn't previously available, such as currency formats, label locations, and count of rows in a table.

To supercharge your AI implementations, Advanced IDP Tools and prompt builder AI skills can be used together to provide generative AI skills with even more detailed information to complete their extraction task. By offering this additional data, we're opening up more processing capabilities for developers to help you manage the most complicated documents your business works with.

### More AI features are now highly available (HA)

High availability for Appian Cloud customers is available in Appian 24.4 and later for generative AI skills, AI Copilot for business users, and AI Copilot for developers. These features provide automatic scaling and redundancy across multiple zones. High availability is also available for the new Advanced IDP Tools AI skill in Appian 25.2 and later. With high availability, your AI workflows are protected against failures and can recover quickly to minimize downtime and ensure continuous access.

### Power high-volume, high-value generative AI use cases with autoscaling

Generative AI skills can now be used in autoscale processes , helping them stay responsive and efficient even when demand increases. Everything is ready to use—no setup required. Just build your process and Appian takes care of the rest.

### Optimize AI usage in your processes with token information

Generative AI skills now output the number of tokens used in each execution, making it easier than ever before to determine how many tokens an application will use once it is deployed to production. By providing detailed token counts for both inputs and outputs to the AI skill, users can better understand and optimize their applications' token consumption, preventing unexpected costs and ensuring smoother and more efficient AI implementations.

## RPA

Robotic process automation (RPA) simplifies how you build, manage, and scale digital workers to handle repetitive tasks across systems. By automating routine processes, your teams can focus on higher-value work that drives innovation and efficiency.

This release introduces optimizations that make robotic tasks lighter and faster, enhancing stability during development and execution—all without increasing infrastructure demands.

### Streamlined robotic task development

Building on our recent advancements, RPA 9.16 introduces significant optimizations to robotic tasks, reducing their size by up to 70%. For example, a robotic task that previously occupied 22MB is now just 6.5MB! This helps large robotic tasks load noticeably faster during monitoring and debugging, allowing for more efficient and responsive development. And thanks to the overall reduced memory usage, teams can now work concurrently on complex projects without requiring additional infrastructure.

We've also enhanced support for nested sub-robotic tasks, allowing for more intricate automations, while optimizing server performance improves stability by lowering hard disk usage.

### Performance enhancements for robotic task execution

The RPA 9.15 release includes key improvements that enhance the overall experience of building and running robotic tasks. Debugging and execution are now more stable, even when multiple users are working simultaneously. Robotic tasks also run more smoothly and responsively, even during complex executions. These updates improve efficiency at scale, allowing teams to develop large robotic tasks together without increasing infrastructure costs.

## Autoscale

Autoscale combines low-code design and business process automation with unmatched scalability. This release, we're excited to introduce timer events for autoscaled processes, as well as features that make it easier to monitor and cancel large numbers of processes.

### Use timer events in autoscaled processes

You can now add timer events to autoscaled processes, making them more flexible and adaptive to your other enterprise systems. Timers allow you to schedule when nodes run or repeat, letting you retry actions for external services that may not be responding as expected.

By adding timer events to your autoscaled process, you can keep your processes running smoothly and allow Appian to resolve issues for you with less manual intervention.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Cancel autoscaled processes using filters

This release, we're giving you more control over how you manage your processes on the Autoscaled Process Activity page. Instead of canceling one page at a time, you can now cancel all active autoscaled processes matching your filters with a single click.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Enhanced monitoring with new filtering and improved navigation

We're also improving process monitoring by adding filters on the Autoscaled Process Activity page. We've separated out the process status and error state filters, giving you finer control over the data shown in the grid and helping you quickly find the processes you're interested in.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

And, once you dig into a process, you can open its parent or child processes in monitoring mode with a single click!

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

## Process HQ

Combining the latest technologies in data fabric, process mining, machine learning, and generative AI, Process HQ gives business users the power to explore data and identify timely insights they can use to optimize their business.

This release, we're making it faster to find and build insights with enhanced field discovery in processes and reports, single-click chart filters, drilldowns right from conformance KPIs, and more!

### Introducing light mode for Process HQ

Now, you can choose the way you view Process HQ. In your Appian user settings , you'll find a new option that allows you to set your theme to light mode or dark mode.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Enhanced field discovery

In this release, we're helping you work more efficiently in Process HQ. Now, when you browse fields to include in a process, report, or filter, you'll be able to search your fields by name, so you can quickly select the exact fields you need.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Interact with charts in data fabric insights

The reports you build in data fabric insights help you monitor your business data at a glance. In this release, we're adding more power to your reports by adding interactive filtering.

Now, you can click on any section of a chart to instantly filter the grid and focus on specific details of your data. With this new feature, you can easily navigate your data and answer important questions about your business.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Tune your views and KPIs with greater precision

In process insights, views and KPIs help you focus on just the right data, so you can monitor process health and spot opportunities for process optimization. This release, you can more precisely refine that focus with added flexibility in filters for views and KPIs.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

You can decide to include cases based on whether a specific activity or sequence is present or not. Or, you have the option to filter based on case duration. That way, you're always analyzing cases that are most representative of your data set and most relevant to your business needs.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Explore more process details at a glance

Process exploration lets you learn how your process actually operates and start seeing the patterns that cause issues. We've surfaced additional details in both your views and KPIs , so you can quickly assess whether a characteristic deserves a closer look.

Now, when you click an activity or sequence in the process diagram of any page, you'll see a full set of visualizations showing you how much that part of the process contributes to inefficiency.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

And, for count, automation type, and aggregation KPIs, you'll see metrics specific to the KPI type. For example, a count KPI will show either case or occurrence counts.

You'll see this type-specific approach in adjusted trend charts…

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

…new columns in the Case Attributes grid…

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

…and updated statistics in the process diagram.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

And if you're curious about how inherited filters are shaping the data you're looking at, you can easily check out a list of the view and KPI filters .

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

With this enhanced exploration experience, you'll always have the relevant process details at your fingertips.

### Drill down on conformance

Previously, we introduced the conformance KPI to give you a quick way to monitor how often activities occur in the expected order. This release, you can drill down directly from the conformance KPI to focus on activities and sequences that don't conform.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

In the drilldown page , you can quickly evaluate characteristics of the related cases and combine them into an actionable insight that can jumpstart conformance gains.

### Alerting on count KPIs

Keeping an eye on your business processes is important. Last release, we made that easier than ever by letting you set thresholds and enable email alerts for duration KPIs. Now, we're giving you the same capability for count KPIs, so you can easily track how your process is performing compared to your expectations.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

## Data Fabric

This release, we're excited to announce some of our biggest data fabric features yet! With the ability to manage documents with record types, schedule incremental syncs, and sync up to 20 million rows of data, you can unify even more of your data in Appian than ever before.

### Bring documents into your data fabric

Appian's data fabric allows you to stitch together data from multiple systems into a single, secure data model, so you can build applications quickly. Now, we're expanding our data fabric and all of its powerful capabilities to support documents .

Starting this release, you can use record types to manage application documents , access document properties , and streamline your document workflows .

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

#### Manage, relate, and secure documents with record types

Now, you can use record types to manage documents, making them more secure and integrated in your applications. We'll even help you get started when you use codeless data modeling to build your application data. With just a click, you can generate a record type to manage documents related to your business data—no folder creation necessary.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

You can then add relationships to relate documents to other application data so you can easily display all relevant information in one place. You can also configure record-level security to provide more granular security around who can see which document. For example, users can only see case documents if they can see the related case.

Plus, when you bring documents into your data fabric, you can use AI-powered features, like smart search and the Document Extraction AI skill , to explore and extract information from your documents.

#### Easily access document properties

Alongside the record type to manage your documents, we'll provide you with an out-of-the-box Document record type to store document properties, like file name, size, extension type, and creation date.

We'll go ahead and set up a relationship for you between your document management record type and the Document record type, so you can use this information to filter, sort, or aggregate documents in your apps.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

#### Streamline workflows to add, update, and remove documents

As an added bonus, using a record type to manage documents means you don't have to worry about folders . Since all document access is controlled by the record type, there's no folder creation, organization, or security needed.

Not only does this reduce the number of objects you need to maintain, it can also reduce the number of steps in your processes—entirely eliminating folder management tasks.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Sync data more frequently with incremental syncs

We know that your organization can have multiple external systems updating data throughout the day, so this release, we're introducing a way to sync those changes more frequently: incremental syncs .

You can schedule incremental syncs on any service-backed record type to regularly capture new or changed data throughout the day. This allows you to sync smaller portions of data more frequently, making fewer API calls and ultimately saving you precious time and resources.

The best part? You get to decide how often those changes are synced based on your business needs—whether it's every few hours or minutes.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Sync up to 20 million rows in each record type

We're committed to helping your data fabric scale with the needs of your organization. That's why we continue to increase the amount of data you can sync in each record type—now up to 20 million rows !

### Make record fields more powerful and reusable

Record fields make it easy to build and interact with your enterprise data, and now, you can further accelerate your app design by adding reusable validations and interfaces to your fields . This allows you to not only efficiently reuse record field configurations and visualizations throughout your application, but also helps to improve long term application maintenance.

Just make a few one-time configurations to your existing record fields and add reusable interfaces or common validations. In a few clicks, you can generate or add reusable user interfaces that define how a record field should look when used in different kinds of interfaces. And, you can configure common or routine validations that will automatically evaluate every time your record field is used.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

Then, simply call the reusable validations and UIs for your record field directly from an interface —no further configurations required! These "set once, use anywhere" record field configurations are a breeze to maintain and allow for convenient, reliable, and uniform reuse.

### New functions to support record field validations

With our enhancements to record field configurations , you can configure common validations on your record fields directly from your record type and use them throughout your application.

We've created the new a!applyValidations() function to help you reference and expand upon those validations in interfaces and expressions. Just use the function in any validations parameter to easily reference the pre-configured validations for one or more record fields. You can even use the function to add in ad-hoc validations that are specific to your interface or expression.

And to save you a step, we'll even go ahead and automatically add the a!applyValidations() function to the input interface you generate for your record field.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

Be sure to also check out the slew of other supporting functions we created to help you get the most out of your reusable validations: a!isBetween() , a!startsWith() , a!endsWith() , and a!isInText() .

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Quickly connect to your data sources

This release, you can curate a list of commonly used data sources to speed up your record type configuration and instantly connect to the data you need. With just a click, you can add any connected system to the data source shortcut list and provide a custom name that's easily identified by you and other developers.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Pick and choose suggested relationships

It's already easy to relate enterprise data using suggested relationships to your record types. Now, we're giving you the flexibility to individually pick and choose which suggested relationships you want.

We've also simplified the generated relationship names so they no longer include the application prefix—making them easier to read and reference in your apps.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Modernized layouts for generated record actions

Last release , we gave generated record actions a fresh look and feel. This release, we're introducing even more improvements to help you make beautiful interfaces quickly and easily.

Now, newly generated record action interfaces will take advantage of our new and improved form layout , header templates , and new dialog size options , so your actions have a modern look and feel the moment they're generated.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

We've also continued making improvements to our smart data generation capabilities. If your record type includes a Document field , we'll automatically include a file upload component . And, if the record type has a one-to-many relationship with other record types, we'll automatically generate the record actions using the brand new wizard layout component .

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

These new tools help you generate better UIs tailored to your data types, so you can create a sleek and efficient experience for your users with even less development time.

### More flexible dialog sizes

This release, we're making it easier to create more functional and modern UIs with more sizing options in record action dialogs. Now, you can control both the height and width separately to create dialogs that fit your specific needs.

We've also updated the default dialog sizes for record actions, so your new record actions will have a narrower width by default.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Easily access interfaces from the record type

We're helping you save time during development by making it easier to access record action interfaces. Now, when you view your record actions, you'll see a link to the start form interface for each action, so you can easily find your interfaces right from the record type.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Support for OAuth 2.0 credentials in data sources and custom JDBC connected systems

We're excited to give you new authentication options to connect your data sources to Appian. Starting this release, you can now use OAuth 2.0 with your SQL Server and Oracle connected systems, as well as custom data sources.

## Our new dynamic duo: the control panel object and the Control Panel workspace

This release we are introducing the control panel object to work in tandem with the Control Panel workspace . The control panel object allows low-code developers to easily define the configurations that no-code developers and business users can make in the Control Panel workspace .

The control panel object is a set of low-code configurations that lay the ground-work and make up the underlying structure of the applications configured in the Control Panel workspace.

Each control panel object contain key foundational information about the applications configured in the Control Panel workspace. This can be anything from the terms to use for cases, to how to organize the overall data structures, or even what types of forms and interfaces can be used.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

And, control panel objects are so highly configurable that they allow you to add customized pages and functionality to the Control Panel in just a few easy steps.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Seamlessly manage objects and security

Not only do control panel objects help you to organize configurations for the Control Panel workspace from the start, but they also help you secure and manage them.

With built-in security configurations, you can easily set which users and groups have access to the categories and types that make up the structure of your Control Panel applications. For example, if you created categories for different departments, you can set security so that only the business users in each department can access the data, forms, and configurations for that category and its types.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

The control panel object makes managing your Control Panel applications easier by acting as a go-between to connect the front-end configurations made by business users and the objects generated in Designer to support them. This helps to maintain the relationship between the records types and interfaces and the no-code experience of the Control Panel workspace, keeping them all connected and up-to-date.

With the combined capabilities of control panel object and the Control Panel workspace, you can empower both low-code and no-code developers to collaborate on mission-critical applications that can continually adapt to meet your business needs.

## Case Management Studio

This release, we're continuing to improve your case management applications and experiences with big updates to Case Management Studio.

### New look and feel for Case Management Studio

Alongside the release of the Control Panel workspace and control panel object in 25.2, we are excited to release Case Management Studio 2.0 ! This major release includes a complete integration of the Control Panel workspace and object framework into the Case Management Studio application suite, fully replacing the Studio site functionality .

This means that the Case Management Studio you know and love is not only getting feature upgrades, but an entirely new modern look and feel.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

The expanded functionality can be leveraged in both the control panel object and the Control Panel workspace . First, your low-code developers will use the new control panel object that comes out-of-the-box with Case Management Studio to lay the groundwork for the configurations your business users can make in the Control Panel workspace. Then, your business users in the Control Panel workspace will build off of that foundation to configure the overall organization, data, interfaces, workflow, and more for your Case Management applications.

Check out some of the new and improved features in Case Management Studio 2.0!

The form builder experience is more powerful than ever, with even more data at your fingertips.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

You now have more control over your data structures and organization with optional use of categories.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

You can more easily add additional customized pages for business users to the Control Panel workspace.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

To learn more about these updates and how Case Management Studio and the Control Panel work together, see the Case Management Studio , the Control Panel workspace , and control panel object documentation .

#### Send emails from your workflow–no human intervention required

Last release, we introduced email templates and the Send Email task type for your case management workflows. This release, we're expanding this functionality with the addition of the Send Email workflow automation. This new workflow automation allows you to send emails directly from a workflow–no human intervention or review required!

Now, you can combine the ease and standardization of email template reuse with the efficiency of automation in just a few clicks.

#### Additional condition options for task assignment rules

This release, we're continuing to help you get the most out of your workflows with two new additions to the conditions for task assignment rules. You can now select Task Assignee and Group Task Assignee as part of the condition for task assignment rules , helping you to create robust conditional logic and more easily adapt to a wide range of scenarios in your workflows.

## Sites and portals

Appian enables you to create superior, seamless experiences across desktop and mobile devices for all your users using portals and sites . This release, we're bringing more troubleshooting information to site objects and displaying more characters in site and portal page names.

### Troubleshoot faster with more visibility into site errors

The new Troubleshoot tab in the site object provides details about errors and allows developers to quickly look into issues without leaving the object. No need to check logs—the error details are right where you need them, in an easy-to-read format.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Even more customization for portal domains

This release, we're enabling you to configure up to 10 custom domains that can be shared among your portals. Have separate portals for registration and customer service? Now you can publish one at registration.portal.com and the other at service.portal.com . Being able to use more domains means you have more flexibility to maintain consistent branding across your portals.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Longer page names in sites and portals

Starting this release, you'll be able to use longer page names in sites and portals without them being truncated, allowing you to provide more context to your users at a glance.

## Interfaces

Appian makes it easy to build beautiful, information-dense interfaces that you can use throughout your applications. This release is filled with tons of impactful improvements, including reusable record field UIs, major improvements to forms, including a new wizard layout, viewing all of your branding configurations directly in an interface object, and more.

### Elevate your form experiences with wizards, title bar templates, fixed buttons, and more!

We're excited to introduce major improvements that will take your form designs to the next level. A new wizard layout, expertly designed title bar templates, fixed buttons, and several input component updates will allow you to elevate the user experience for all your forms.

#### Make magic with wizard layout

In mission critical applications, you may need a lot of information from your users. To make this easier, we're introducing a wizard layout to help you turn your complex forms into clean, modern multi-page wizards that are both beautiful and easy to use.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

In just a few clicks, you can configure this out-of-the-box component with the milestone style and title bar templates of your choice. And, we'll handle all of the step navigation logic for you, so you can create a simple, streamlined experience for your users in a snap.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

#### Introducing configurable title bars for form and wizard layouts

This release, we're excited to announce title bar templates for form and wizard layouts, giving you more flexibility to customize form titles. These expertly designed templates allow you to add formatted text, background colors, icons, and images to the top of your forms with just a few configurations. And, you can even create custom title bars using card and billboard layouts.

We've also added the ability to quickly switch between the different title bar options in design mode with just a click.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

And, a new AI-powered suggestion button can even provide ideas for relevant icons based on the title bar text.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

For more information about how we've evolved form layouts to work with title bar templates, see the evolution release note .

#### Fix buttons to the bottom of forms and wizard layouts

We're also introducing a new fixed button parameter to form and wizard layouts. Now, you can determine whether you want your buttons at the bottom of the page or directly after the page content.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

#### Freshen up your designs with updated interface templates

This release, we've also refreshed our interface template options to showcase our most up-to-date best practices, making it a breeze to build sleek, user-friendly experiences.

We've updated our form templates to take full advantage of the latest form and wizard capabilities, as well as streamlined the page template selections to help you find the right starting point for your designs. And we've also enhanced our Request Form and Short Form example templates, to help you get up and running quickly.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

#### File upload improvements

This release, we've enhanced the file upload component to make the user experience more flexible and efficient. Users can now quickly copy and paste files directly into the upload component. And, we've improved the blocked file extension behavior to remove unexpected validations.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

#### More text formats in the styled text editor component

In this release, we're adding even more utility to the styled text editor component . Now, users can apply superscript and subscript formatting to text in the editor.

#### Control the position of radio buttons and checkboxes

We're giving you another option for displaying radio buttons and checkboxes . A new choicePosition parameter allows you to choose whether to align radio buttons and checkboxes to the left or right of choice labels, providing more design flexibility.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Reference reusable record field UIs in interfaces

With our enhancements to record field configurations , you can create reusable UIs that define how a record field should look when used in read-only and input interfaces. Then, you can easily pop them right into an interface! Just use a record type field reference in your expression to call the record field UI directly into the interface. And, you can even reference record field properties to use your record field display name and description throughout your app.

By improving both the ease and speed of configurability, we're making reusing your most record field configurations a breeze.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Seamlessly view site and portal branding configurations in interface objects

Branding configurations in site and portal objects unlock a world of customization possibilities for your end user experiences. Now, you can see all your branding configurations come together without ever leaving the interface object.

The new branding preview in interface objects empowers you to instantly visualize how your interfaces will look with all of your branding options. No need to switch to the site or portal to see the final styling, just select the site or portal from your interface and watch as the input and dialog shape, button shape and capitalization, and accent color are all applied.

And that's not all. Now, when you configure a custom typeface in the Admin Console, we'll automatically use that typeface in all of your interface objects.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Even more performance improvements for interface objects

Last release , we improved performance for interface objects. This release, we're continuing that mission with even more performance improvements. You'll notice speedier performance when working in interface objects, such as when dragging and dropping elements, configuring parameters in design mode, and viewing updates in live preview.

### New stamp shapes

We've added a new shape parameter to the stamp field component, giving you more ways to display decorative icons and text in your interfaces. Now, your stamps can be round, square, or square with rounded corners.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Updated milestones

In this release, we've added some new enhancements to the milestone component . Milestones can now show longer step names, so you can use exactly the text you need to help orient your users.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

## Appian Mobile

Appian Mobile enables users to monitor, collaborate, and take action on their applications, all from the convenience of their iOS and Android device. This release continues our mission to provide a reliable and trustworthy mobile experience.

### Persisted end user experiences in Appian Mobile

When a mobile device closes the Appian Mobile app in the background, users will now be able to pick up right where they left off. Mobile operating systems often close apps running in the background to optimize resources. Now, if the operating system closes Appian Mobile, users who were working on a site page or offline-enabled task will be taken back to the place they were working for seamless continuity of their work.

### Print actions and tasks directly to PDF on Android

Previously available only on iOS devices, the print to PDF option is now also available on Android. This button gives users the ability to quickly and easily share forms in just a few taps.

### Audio recording available on Android devices

Previously only available on iOS devices, audio recording is now available on Android devices. Now, when users capture video in Appian Mobile on Android, the app will prompt the user to allow audio recording.

### iOS18 navigation improvements for iPad devices

Starting with this release, when users access Appian Mobile on iPads that are on iPadOS 18, they'll notice some subtle changes to the navigation experience. Now, site pages will display in the app header via a floating tab bar, making better use of the larger iPad screen and aligning with the new iPadOS navigation design.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

## Administration

Each release, we continue to give administrators more control over how they manage, secure, and administer their Appian environments. This release, we're giving admins the option to configure additional OpenID Connect providers, the tools to unarchive processes without leaving Appian, and new endpoints for the Cloud Database Management REST API.

### Set up multiple OpenID Connect providers

Organizations often use more than one identity provider to manage user information across their enterprise. With this release, Appian now supports multiple OpenID Connect (OIDC) providers in each environment.

Any user in a configured OIDC provider can sign in to Appian using their enterprise credentials. Check out OpenID Connect User Authentication to get started.

### Unarchive processes in the Process Activity view

Running the archive process script directly on the file system is no longer necessary to unarchive processes. Instead, you can now use the Process Activity tab to unarchive any archived process with just a few clicks.

For Appian Cloud customers with sites created on 21.1 or later, you'll spot an Unarchive button right away. If your site was built on an earlier version of Appian, contact Appian Support to enable this feature. And for self-managed customers, you'll just need to take a couple extra steps to enable the ability to unarchive your processes.

### Manage EDP read access control programmatically

Enhanced data pipeline (EDP) lets you retrieve data from your Appian cloud database and use that data in other systems in your enterprise. Starting with this release, you can use two new REST endpoints to manage the database user's read-access privileges to individual tables or whole schemas—making it easier than ever to automate your app deployments as part of your DevOps process.

### Graceful shutdown

The graceful shutdown period for Appian on Kubernetes and Linux self-managed deployments has changed from 60 seconds to 65 minutes to accommodate system work currently in progress. However, Appian on Kubernetes users can continue to customize their wait period with the grace-period parameter.

## Resolved general issues

- AN-309633 - Medium Fixed an issue causing incorrect number of borders in Card group layouts on mobile.

- AN-308376 - Medium Skipping the warning about Appian authentication password expiration will now redirect users to the Appian Mobile app.

- AN-301527 - Medium Logging out of Appian will now redirect native authentication users to the correct login page, even when the environment has an OpenID Connect provider enabled and Remember IdP for non-SAML users selected.

- AN-313750 - Low Fix version comparison for process reports to reflect changes between versions.

- AN-308572 - Low Improved the performance of sites that have pages with visibility configured as an expression.

- AN-308518 - Low User Management audit log now includes users created using the Create User Smart Service.

- AN-304545 - Low Error message is shown when user attempts to edit an invalid value on the Data Preview tab in a record type

- AN-304126 - Low The tomcat-stdOut.log no longer shows an incorrect warning for site page width.

## Resolved accessibility issues

- AN-312103 - High Fixed an issue where contents within the Edit Profile dialog were not reflowing at high zoom levels.

- AN-311529 - Low Improved the accessibility of changing user and cover photos by updating the save button wording to be more clear.

- AN-302241 - Low Added additional supported values for the text field input purpose parameter.

## Evolutions

The following functions, components, or smart services have newer, improved versions in this release. Existing, old versions in your applications will continue to function normally, but will be renamed on upgrade to indicate that they are older versions. As always, make sure you are using the right version of the docs for your version of Appian. See Function and Component Versions for more information.

### Form layout

The form layout was evolved to implement the new title bar templates . We've made the following changes to parameters to accommodate the new title bar design experience, as well as to align the parameters with wizard layout.

Additional updates:

- We've reorganized the parameter order and design view  and introduced dynamic defaults for certain parameters.

- The default behavior for contentsWidth , showTitleBarDivider , and showButtonDivider parameters will automatically adapt based on if the form is displayed in a dialog or not.

- The title bar divider's width depends on the isTitleBarFixed parameter: If isTitleBarFixed is false, the divider's width matches the content width. If isTitleBarFixed is true, the divider extends to the full width of the screen or dialog.

- If isTitleBarFixed is false, the divider's width matches the content width.

- If isTitleBarFixed is true, the divider extends to the full width of the screen or dialog.

## Deprecations

The features listed below are deprecated and will be removed in a future release of Appian. Do not begin using deprecated features, and transition away from any prior usage of now deprecated features. Where applicable, supported alternatives are described for each deprecation.

### Quick Apps Designer

The Quick Apps Designer is deprecated and will be removed in a future release. Applications created using quick apps will continue to function.

You can speed up your application development by using Appian's data fabric features to quickly generate database tables , record actions , and record views . And starting this release, customers with Case Management Studio and select solutions can empower business users to configure data and interfaces using the new control panel.

### End-of-support for older versions of RDBMS

The following relational database management systems (RDBMS) either have already reached or are approaching the standard end-of-support dates set by their vendors and will no longer be supported in a future release of Appian. Customers are strongly advised to upgrade to a newer supported version .

## Removals

The features listed below have been removed from Appian and can no longer be used.

### End-of-support for older versions of RDBMS

The following relational database management systems (RDBMS) have already reached the standard end-of-support dates set by their vendors and are no longer supported in Appian.

### End-of-support for older VPN encryption algorithms

The following VPN encryption algorithms will be reaching end-of-support and are no longer supported in Appian Cloud VPN tunnels. Customers are strongly advised to upgrade to newer supported algorithms as soon as possible.

### Public IP Addresses over DNS-based VPN Routing

Appian Cloud offers the ability to use VPN tunnels to connect your self-managed resources to your Appian Cloud environments. If you are using a private DNS server accessed over the VPN tunnel to resolve FQDNs, and the IP addresses to which the FQDNs resolve are public IP addresses, traffic to the public IP addresses will now be sent over your VPN tunnels. Previously, Appian Cloud sent this traffic over the public internet. Sending this traffic over the public internet by default is no longer supported. If you believe you are impacted by this end-of-support announcement, please reach out to Appian Support to determine if there is a workaround that can be applied to your VPN configurations.

## Feedback


---

## Appian 25.4 — synced 2026-08-16

Source: https://docs.appian.com/suite/help/25.4/Appian_Release_Notes.html

# Appian Release Notes

Share via

LinkedIn

Reddit

Email

Copy Link

Print

25.4 Release Highlights

Join our Appian Community team and other Appian experts as they dig into highlights from the 25.4 release.

Join our Appian Community team and other Appian experts as they dig into highlights from the 25.4 release.

## Release highlights

This release introduces many new and exciting features throughout the platform that help you improve the scalability, speed, and performance of your applications.

We're particularly excited to shine a spotlight on three standout features this release, which accelerate your applications development and easily integrate AI into your workflows.

### Appian Composer is generally available

We're excited to share that Appian Composer is now generally available in the Appian platform. Previously introduced in Appian 25.3 , Composer is an AI-powered capability that transforms how you plan and build your applications.

Building on Composer's existing capabilities, this release makes it possible for you to upload requirements documents in multiple formats, making it easier to kick off planning right away. It also introduces support for business rules and workflows , which helps you stay aligned with stakeholders before and during development.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### AI agents that supercharge your process automation

Meet AI Agents , Appian's latest advancement in AI-powered process automation.

AI agents introduce a groundbreaking new way to automate your most complex workflows. Instead of coding every step, you can now provide high-level goals in plain language and let your AI agents do the rest. They intelligently reason and adapt, using your existing data fabric and design objects to determine the best path forward—all with the transparency and security your enterprise demands.

Agents can interpret unstructured data like emails, make real-time decisions, and dynamically change course. This makes them perfect for unpredictable scenarios such as triaging cases, resolving vendor issues, or routing support requests. For example, an agent can read an incoming email, reference your standard operating procedures, and automatically route the case to the right team.

With AI agents' powerful new approach, your automations become smarter and more adaptive, allowing you to expand what's possible with automation.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

## AI in process

Go beyond traditional automation with Appian's AI capabilities.

AI skills let you build and configure artificial intelligence (AI) models for use in your processes. In this release, you can unlock the latest AI models with inference profiles and use generative AI at high volumes without interruption.

AI agents take process automation even further by handling dynamic, complex tasks. Now, you can assemble autonomous AI agents and equip them with a variety of powerful tools to optimize your workflows.

### Unlock the latest AI models

Appian continues to make it easy to access the newest and most powerful AI models. In the Administration Console , you can configure which models and profiles your organization uses—no support case required!

This feature allows you to use the most advanced models, like Sonnet 4, while ensuring transparency and compliance in your data flows. Some AI capabilities in Appian automatically use the models you select ; however, you must manually upgrade AI skill objects to leverage the latest models.

We recommend enabling Sonnet 4 today, since Sonnet 3.5 will be removed in a future release.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Select the perfect AI model for your use case

Take full control of your AI-powered applications. You can now select the specific generative AI model used by your AI Skills directly in the prompt builder AI skill.

This new model selection feature gives you the transparency and flexibility to choose from a list of enabled models available in your region. For your most complex use cases, you can select more powerful models to achieve higher accuracy and get to production faster. This increased visibility also supports enterprise governance requirements and simplifies debugging by making model usage clear across your applications.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Handle long-running AI Skill executions without timeouts

The Execute Generative AI Skill smart service now has an option to process longer AI skill responses from even the most complex inputs without worrying about timeouts.

You can choose to run the smart service in Standard mode for smaller executions, or in Long Running mode to give long-running executions the time they need to finish. We're giving you the flexibility you need to tackle your most demanding use cases with confidence and continuity.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Quickly discover your available generative AI models

Now, you can see the specific generative AI models available in your environment by using the new a!genAiModels() function —helping you to build more flexible applications or solutions. For example, You can see this function at work in the AI Document Center where it's used to display the list of available models for extraction or classification and for AI review. Now, you can experiment with and deploy the latest models to solve your unique business challenges faster.

Additionally, the Execute Generative AI Skill smart service now supports runtime model selection that overrides the model configured in the AI skill, giving you even more flexibility to choose the right model for each execution.

## Appian AI Copilot for developers

AI Copilot helps developers be more productive. This release we're excited to announce that Appian Composer is now available as a full part of the Appian platform.

Composer now lets you upload requirements documents in multiple formats, making it easier to kick off planning right away. It also introduces support for business rules and workflows, which helps you stay aligned with stakeholders before and during development.

### Upload your requirements into Composer

Composer now supports direct uploads of your requirements in TXT, DOC, DOCX, or PDF format. It automatically transforms your documents into a clear, detailed application plan right in Composer, so you can move from requirements gathering to application planning with more confidence and faster results.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Business rules are now part of the planning process in Composer

Business rules are now part of your application plan. AI turns your requirements into suggested business rules that capture your application's decision logic, making it easy to generate expression rule objects with one click.

Composer keeps your business rules visible, enables easier alignment with stakeholders, and makes it easier to adapt as priorities change.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Unlock faster automation with Composer and process model generation

It's never been faster to bridge the gap between business requirements and a functional application. Composer now provides a process diagram that clearly shows your entire process, complete with swimlanes for each persona and a clear sequence of user activities and automated activities. This makes it easy to align with stakeholders early and ensure everyone has the same understanding before development begins.

With one click, you can turn the process into multiple starter process models that include user tasks, gateways, and smart services. The process models are ready for you to refine and fine tune, jump-starting your development process.

By seamlessly transitioning from a visual process to starter process models, you can ensure a more accurate path from planning to execution. This combination supercharges your development lifecycle, ensuring your ideas become applications faster than ever before.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Generate a Reports and Dashboards Library page with Composer

Composer can now automatically generate a Reports and Dashboards Library page for your Appian Site , helping you bring Process HQ to your users faster than ever. Now, you can give your users access to everything they need to manage reports and dashboards with even less development time.

## Appian AI Copilot for business users

AI Copilot provides capabilities that developers can enable to make Appian applications more intuitive and efficient for business users. These features highlight how developers can configure and extend AI-driven assistance in their apps, helping business users work faster, make better decisions, and reduce manual effort.

This release we're introducing a new, customizable chat component and expanding the regional availability of AI Copilot to our customers in Europe.

### New chat field component

Create unique chat experiences in Appian with the new chat component . It's fully accessible, customizable, and built to grow with your needs—whether that means adding chat persistence, enabling multiple threads, or tailoring interactions for your users.

As part of this new capability, we're also introducing the a!callLanguageModel() function that directly connects your chat component to Appian's built-in language model. This makes it simple to send user messages and history to the AI model and display its dynamic, generated response right in your interface.

Now you can design chat solutions for your most complex use cases and deliver the modern, responsive conversations your users expect.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Access AI Copilot features in more regions

This release, we're expanding the regional availability of AI Copilot to our customers in Europe. You can now leverage Enterprise Copilot , Documents Chat , and smart search in the Europe (Zurich) region.

## Data fabric

Appian's data fabric stitches together data from multiple systems into a single, secure data model, so you can build applications quickly.

This release, we're excited to announce that you can sync more data per record type, use synced record types in your high throughput automation workflows, and take advantage of new smart search configurations.

### Sync up to 50 million rows per record type

We've increased the number of rows you can sync in each record type to 50 million ! This increase ensures that your data fabric can scale with your business needs, while maintaining the consistent and reliable performance you expect in your applications.

### Use synced record types for high throughput automation

Not only have we increased the number of rows you can sync in each record type, we've enhanced our data fabric architecture to support concurrent write processing. With this improved foundation in place, data fabric can achieve over 5x higher write throughput—allowing you to use synced record types to support high volume transactional workloads with up to 30,000 transactions per minute.

### Secure your synced data with transparent data encryption

Appian now supports transparent data encryption for synced record types , enhancing the security of your enterprise data without requiring changes to your applications. With this update, synced data is automatically encrypted in the data service using industry-standard encryption protocol. This adds an extra layer of encryption on top of storing data in securely encrypted devices.

This capability strengthens your organization's compliance posture and ensures sensitive data is protected, even if access to the underlying storage is compromised.

### Skip additional sync failures

Make your record data more resilient with Skip failed smart service syncs . With this new sync option, the record type will skip any failed smart service syncs and continue using the previously available data.

Not only does this option keep your business critical application running without interruption, but you can be confident that any skipped changes will be synced during the next full or incremental sync.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### More intuitive similarity scoring for smart search

Smart search transforms how you search through your synced record types. This release, we've made the similarity scores in smart search more intuitive so it's easier to fine-tune and control search results in your applications.

Now, when you enable smart search in a read-only grid or an a!queryRecordType() expression , you can use a simplified numerical range to determine whether more search results are returned or only the most similar search data.

### Keep smart search online with configurable indexing failure tolerance

You can now configure an index failure tolerance level to make smart search more resilient. You can use this setting to keep smart search to stay online, even if some rows fail to index. This helps prevent minor data issues from disabling smart search functionality across the entire record type.

You can pick the tolerance level that works for you, from strict in production environments where accuracy and data integrity are critical, to a relaxed setting in development environments where search completeness isn't needed.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Smart search indexing with incremental syncs

Smart search now updates automatically whenever an incremental sync occurs on the record type. This guarantees that you and your users are automatically searching through the latest data, regardless of whether it's from a full or incremental sync.

### Monitor disk space for documents stored in Appian

You can now easily monitor how much disk space is used by the documents in your record types. From the Documents page , you can see a breakdown of disk space used—including how much space is taken up by unused documents. With this new insight, you can make more informed decisions about cleaning up your documents to save valuable resources.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Access more document properties

We've added additional fields and relationships to the out-of-the-box Document record type to show who created a document, who last modified it, and when. And, with relationships to the User record type, you can quickly learn more about the users who manage documents in your applications.

To take advantage of these data modeling enhancements, simply update the Document record type .

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Easily monitor and manage users

We've made it easier to get a complete picture of the users in your environment with enhancements to the User record type and the Users page in the Admin Console.

The User record type now displays more information about your users. You can query details like user locale, time zone, and last login time, leveraging data that was once only available through User Properties .

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

We've also added new status and last login information directly to the Users page in the Admin Console , letting you see if a user is active, inactive, or locked at a glance. Appian can also automatically update a user's status based on their last login date, automating key administrative tasks so you can focus on what matters most.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Accelerate development with improved record action generation

We're making generated record actions even smarter to help you build better apps, faster. Now, record action generation automatically recognizes all your record type relationships while continuing to choose the best input style based on all the nuances of your varied data.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

We've also updated the existing "record" variable to use a more descriptive, camel-case name that follows best practices by default. This can be customized when generating record actions and views, saving you from manual refactoring.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Unlock complete design freedom for record views

Take full creative control of your record views! We've added a new option that lets you hide the out-of-the-box record header , including the title, tabs, and actions, giving you complete freedom over the user experience. This allows you to use the entire page to display your own custom header, ensuring the design perfectly matches your branding and style requirements.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Translate reference data for individual records

Last release, we added the ability to generate multiple translation strings for lookup data directly within the record type.

This release, we're adding the ability to create translation strings for lookup data in individual records, or even use existing translation strings. There's no need to go through the bulk generation flow for just one record—–now you can add and update your lookup data as you go.

This helps you to ensure that all of the necessary record field values are translated, even if a record was added after the initial translation strings were generated.

### Reduce duplicate translation strings for choice list fields

Last release, we also introduced generating translation strings for choice list fields . We've improved this feature to now check the choice list options against the existing translation strings in the translation set and alert you to possible duplicates.

Reducing the number of duplicate translation strings helps you to limit confusion for translators and keep your translation sets clutter-free.

### Quickly monitor data syncs

We've made it faster and easier to monitor your data syncs using the Record Sync Status tab in the Monitor view. Now, you'll notice a significant performance boost on this tab, ensuring it loads in a flash even with thousands of record types.

To make troubleshooting a breeze, you can use new search and filter options to instantly find record types by sync status and source type. We've also added a new Last Sync Type column so you can immediately see how each sync was initiated.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### New system log for tracking data fabric metrics

We're introducing a new metric log, data-fabric.csv , to collect and analyze your record type usage. This log uses a simple four-column format, so you can quickly filter and find the information you need. Going forward, this will be the new home for all data fabric metrics instead of the records.csv log.

### Request scopes when refreshing tokens with OAuth 2.0

To continue accessing data, some external data sources require the scope to be sent alongside each refresh token request. With just one click, you can now configure HTTP and OpenAPI connected systems to automatically include the scopes on refresh.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

## Autoscale for process

Autoscale combines low-code design and business process automation with unmatched scalability. In this release, we focused on making it easier to find and fix errors in your autoscaled processes. We've improved error visibility and diagnostics with a new dashboard, and we're providing new tools for stopping processes at scale.

### Get to the root of process errors faster

To help you on your journey to automate your high-scale business processes, we're excited to introduce new tools for fixing errors. Now, you can launch a new error dashboard directly from the links in the process alert emails. This view breaks down all errors by node and error type, giving you a comprehensive picture of any issues with your processes.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

And, if your error can be fixed by modifying process variables or skipping or restarting a node, you can now do so directly from monitor mode , letting you get your processes back on track in a flash!

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Cancel queued processes

When working at scale, you might need a way to quickly stop runaway processes, including processes still waiting in the queue. Now, when you cancel a group of processes, you can also clear the queue for that process model. This ensures all work is halted immediately, so you can make changes to the model and get your mission-critical work back on track without delay.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Expanded data protection options for autoscale

We're committed to giving you a range of options for managing your data in Appian Cloud, so this release we're expanding the ways you can control data used by your autoscaled processes. You can now opt in to a dedicated virtual private cloud (VPC) or bring your own key (BYOK) to encrypt your business data. Contact your Appian account executive if you are interested in enabling either of these features.

## Process HQ

Combining the latest technologies in data fabric, process mining, machine learning, and generative AI, Process HQ gives business users the power to explore data and identify timely insights they can use to optimize their business.

This release, business users can leverage AI Copilot to quickly build reports, developers can deploy reports with applications, and all of Process HQ is highly available. Plus, your business users can enjoy improved filtering of reports and dashboards in sites, building reports across one-to-many relationships, and using new duration filters for a more refined process analysis.

### Create reports instantly with AI Copilot

Building custom reports in Process HQ is now as simple as chatting with AI Copilot . Just describe the insights you want, like "Show me total customers over time, grouped by quarter" or "What is the breakdown of customers by industry?" and AI Copilot will generate a chart preview right in the chat.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

You can keep chatting to adjust the chart type or apply filters, such as "Only show the past year". Once you're ready to edit the report yourself, just click to jump in, make changes, and save the report.

Plus, AI Copilot is now available on the Process HQ home page, so report creators explore data and create reports right away.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Deploy reports and dashboards with your applications

This release, developers can deploy reports and dashboards with their applications, so they can be displayed on sites or used to build other custom reports. Now, the people who know your data best can collaborate easily with the people who need that data most.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Process insights is now highly available

Process HQ has always supported data fabric insights in high availability (HA) for Appian Cloud customers , and now, we're adding support for process insights as well. With high availability, your workflows are protected against failures and can recover quickly to minimize downtime and ensure continuous access.

### Curate the Reports and Dashboards Library for your sites

You can now provide a tailored reporting experience for your site users . Simply configure a Reports and Dashboards Library page in your site to filter on record types relevant to specific applications. We'll then filter the library to show only the reports and dashboards based on those record types. This ensures your users can quickly find the information they need without the clutter from other applications.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

We've also added support for Process HQ site pages in Appian Mobile , so users can access these curated insights wherever they work.

### Easily report across one-to-many relationships

Unlocking insights from your complex data is now simpler than ever. Now, you can build reports starting from the "one" side of a one-to-many record type relationship and easily include fields from the "many" side. This makes it possible to join tables directly in your reports, even when working with many-to-many relationships . This empowers business users to connect data across multiple record types without taking up developer time.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Sharing at scale

Report editors can now share reports and dashboards with groups. This way, you'll spend less time managing access and more time collaborating with even more users across your organization.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Cut through the noise with new duration filters

This release, you can filter your views and KPIs based on how long specific activities or sequences take to complete. With these new options, you can easily remove extreme cases that might distort your analysis, so you can zero in on the systemic inefficiencies that matter most.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

## RPA

Robotic process automation (RPA) simplifies how you build, manage, and scale digital workers to handle repetitive tasks across systems. By automating routine processes, your teams can focus on higher-value work that drives innovation and efficiency.

### Enhanced RPA stability for enterprise-scale automation

Appian RPA is now more robust, bringing greater stability to your largest and most critical automation programs. These improvements specifically benefit those who run hundreds of robots, thousands of robotic tasks, and are processing millions of executions. This update ensures Appian RPA stays dependable and helps you manage your digital workforce with confidence.

### Up to 90% faster load times in the RPA console

The RPA console now loads robotic tasks up to 90% faster, delivering a superior experience for users managing thousands of robotic tasks.

We've also simplified filtering in the RPA console so that robotic task runs are only filtered by name and priority. This helps the RPA console align with the straightforward filtering in Appian Designer and provides a consistent experience throughout.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

## Control Panel

The Control Panel is a workspace for business users to make no-code configurations to data, interfaces, and more. This release, we're helping you more closely manage your Control Panel workspace and objects with improvements to deployment, object deletion, diffs and versioning, and reordering configurations.

### Better manage your categories and types

This release, we're improving how you manage your categories and types throughout the Control Panel application lifecycle. Each category and type is now its own object, called a control panel hierarchy item.

Since control panel hierarchy items are individual objects, they can be deployed separately from the control panel object—–allowing you to develop and iterate more quickly. For example, maybe the category for the IT department is ready but the category for the Finance department still needs some work. You can deploy the IT department category to production and get started using it right away, while continuing to improve the Finance department category.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

And, developers can now easily delete control panel hierarchy items as needed. This not only helps ensure that your Control Panel workspace and object only include what you need, but also helps keep your space clutter-free.

As an added bonus, there's no change to how categories and types are created and configured, so you and your business users get the same familiar user experience with all the benefits of control panel hierarchy items being their own objects.

### Iterate on control panel objects with confidence

Continuing our theme of more streamlined development and deployment for the Control Panel, we've added diffs and versioning to the control panel object.

Now, developers can quickly view a previous version and see what's changed in the object. This gives you the confidence to iteratively develop and deploy without fear of making breaking changes, and ultimately leads to more robust applications.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Easily rearrange custom configurations

This release, we're giving you even more control over where each custom configuration appears in the Control Panel workspace. Now, you can re-order the custom configurations in the control panel object so that they appear in just the right order, helping you to craft an ideal experience for your users.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### New and improved modules for Case Management Studio

We're excited to announce that all Case Management Studio modules are now compatible with Case Management Studio 2.0!

We've not only updated the modules to work with 2.0, but we've expanded the Case Creation via Email module. And, we've added two net-new modules to further extend your application functionality: the Knowledge Base module and AI Smart Search module.

#### Communicate case details with ease

In the Case Creation via Email module , case workers can now send emails from an existing case, even if the case was not initially created from an email. And, they can leverage email templates to help them get email threads started faster. These improvements give case workers more tools to efficiently communicate with everyone related to a case, even if they are outside of your organization.

#### Help users find case resources fast with Knowledge Base

Introducing the new Knowledge Base module . This module allows business users to create and upload reference materials, and relate them to a case type or category—all from the Control Panel workspace. The reference material is then displayed in the case summary, putting the resources and context case workers need right at their fingertips.

#### Search with the power of AI with Smart Search

And last but not least, we're introducing the new Smart Search module, backed by the Appian platform's native AI capabilities. Want to find cases and tasks similar to those you're working on? Not a problem. Need to find a past case that you can't quite remember the exact name of? Now, you can use semantic search to find relevant all cases and tasks within a dedicated Search tab—providing a more well-rounded, effective, and helpful search experience.

## Sites and portals

Appian enables you to create superior, seamless experiences across desktop and mobile devices for all your users using portals and sites . This release gives you more control over your site's navigation and powerful new integrations to track engagement and provide in-app guidance.

### Customize your navigation for a seamless user experience

This release, we're giving you more flexibility to design the perfect navigation experience for your users. The all-new Oxygen header bar style offers a fresh, modern look with right-aligned pages and a subtle selection animation.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

Beyond a new style, you have more granular control over the navigation bar's details. You can now manage page label capitalization, decide whether to display your logo, and control the visibility of user profile and settings links in the user menu.

These enhancements provide the flexibility you need to create polished, professional applications that deliver the perfect user experience.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Track and optimize portal engagement with external analytics

Get a complete picture of your portal traffic by easily integrating your portals with Google Analytics and Adobe Analytics. Simply enter your credentials to start collecting detailed usage data, such as where users come from, what they click on, and how many of them visit. Use this data to see what's working, measure campaign success, and create a better experience for your users. This integration provides the key information you need to measure campaign success and improve the user experience across your portals.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Easily integrate WalkMe for in-app guidance

Improve user onboarding and training for your applications with the new WalkMe integration. If you use WalkMe, a digital adoption platform, you can now enable it directly from the Admin Console to activate powerful, in-app guidance in sites and portals to help your users master your mission-critical applications.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

## Interfaces

Appian makes it easy to build beautiful, information-dense interfaces that you can use throughout your applications.

This release supercharges your design experience with a reimagined configuration pane, powerful new document management capabilities, and even more accessibility and performance improvements.

### Design faster with a reimagined configuration experience

We've completely reimagined the component configuration pane to make your design mode experience faster and more intuitive. Parameters are now neatly organized into logical tabs like Data and Styling , and a new search bar lets you find any configuration in an instant. We've also reduced clicks by letting you add multiple nested items directly from the parent component. And, new breadcrumbs make navigating between components a breeze.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

Building on the visual updates from last release, we're also continuing to expand the use of our modern parameter controls. We've replaced dropdowns on dozens more parameters with icon and text controls that show all your options at a glance.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

We've also simplified the process of entering custom hex codes in our new color picker , making your design workflow faster.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

We've even streamlined a common input configuration; now when you select a variable for Display Value , the Save Into parameter automatically updates to match.

These enhancements, combined with the pane's new structure, make it easier than ever to craft the perfect design in a fraction of the time.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Instantly preview Microsoft documents in record views

We've made it easier to display Microsoft Office files for your document management record types . Now, when you generate a record view for that record type, it automatically uses the existing Microsoft Document Editor plug-in to display previews for Word, Excel, and PowerPoint files.

And, if a document can't be previewed on a specific browser, the component allows users to easily download the document so they can access the information they need.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Go straight to the source with document highlighting

The document viewer component now supports direct navigation and text highlighting, eliminating the need for third-party plugins. Chrome and Firefox users can now see the document viewer automatically open to the correct page and highlight the exact source text, making it easier to validate content and streamline workflows.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Preview, download, and edit uploaded documents with ease

We've enhanced the File Upload component to make it easier to enable common file management capabilities. Now, you can use the documentActions parameter to enable common actions like previewing, downloading, and renaming files and descriptions with a few clicks.

You can also use the dropZoneStyle parameter to configure a larger, more prominent file upload area—making it easier for users to quickly drag and drop files.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### More targeted async loading placeholders for rich text and grids

We've improved how rich text display components behave when loading their data asynchronously using a!asyncVariable() . The async placeholder now appears directly on the rich text display component itself, instead of on the entire layout containing it. This is especially powerful in read-only grids . Now, when you use an async rich text component in a column, that column will load asynchronously from the rest of the grid. This more targeted loading means your users can see and interact with more of the page while the rich text content loads.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Enhanced accessibility for keyboard navigation

Navigating your applications with a keyboard is now easier and more accessible. We've introduced a more prominent focus indicator for various UI elements like links and tooltip icons, making it easier for users to spot the keyboard focus and helping you deliver a more inclusive user experience.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### More options for predefined colors in card layout

Designing with card layouts is now more flexible and consistent. We've added two new predefined color options, "WARN" and "INFO" , to the decorativeBarColor and borderColor parameters.

### Build faster with a more performant design experience

We're continuing our goal to provide you with a faster design experience for interfaces. We've sped up your design experience, making common actions like opening interface objects, saving changes, configuring components, and closing dialogs feel quicker and more responsive. We've also extended the performance boost for saving changes to all other design objects, so you'll enjoy that extra speed no matter what you're building.

### Simplified interface object menu

We've tidied up the interface object menu to create a more focused experience. The Save As menu option will now only appear for developers who have access to Tempo , ensuring you only see relevant options.

## Appian Mobile

Appian Mobile enables users to monitor, collaborate, and take action on their applications, all from the convenience of their iOS and Android device.

### Introducing a more seamless mobile app update experience

We've streamlined the experience for users when they need to update their app to comply with the required minimum app version .

Users will now see a sleek, full-screen page that matches your custom branding, links directly to the app store, and feels more modern.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Enjoy a more intuitive data sync experience

We've made the data sync experience more streamlined for offline mobile. When users complete a data sync and return to an offline site page they were previously on, we'll automatically refresh it for them—no need for a manual update.

### More improvements to persisted end user experiences

Building on the recent improvements to mobile recovery for site pages and offline-enabled tasks, we've now extended this capability to record views on iOS. If the app closes in the background while users are viewing a record, they'll be taken right back to that record when they reopen the app.

## Administration

Each release, we continue to give administrators more control over how they manage, secure, and administer their Appian environments.

### Support for new locales

We're excited to announce that Appian now supports 10 additional locales, so you can provide your users with a best-in-class experience in their preferred language and locality.

You can find these newly added locales in the Internationalization section in the Admin Console :

- Czech

- English (Australia)

- English (Canada)

- English (New Zealand)

- English (South Africa)

- German (Austria)

- German (Switzerland)

- Hungarian

- Romanian

- Slovak

### Secure user accounts with authenticator apps

We're excited to announce enhanced multi-factor authentication (MFA) support , bringing greater security to your Appian system. Now, you can require a one-time code from an authenticator app like Google Authenticator, Microsoft Authenticator, or Authy, adding a powerful layer of protection when users sign in.

### Separate timeouts for administrators and users

This release, we're giving you more control over user session timeouts . Now, administrator accounts and user accounts can have different timeout values. This means you can enforce specific security requirements for each type of user, enhancing overall security and flexibility within your Appian environment.

Additionally, the configured session timeout value now accurately reflects the total time before a user is signed out, so organizations with strict compliance requirements can trust that the timeout matches their documented policy.

### Easily view object UUIDs

We added the object UUID to the properties dialog, making it easy for low-code developers to reference objects while building applications. This is available on all objects except AI skills, robotic tasks, and robot pools.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Logging

The schema for the login-audit.csv log has been updated to provide better enforcement and visibility into multifactor authentication metrics.

The following changes were made:

- The file now includes a header row for all columns.

- The MFA User column has been renamed to MFA Authenticated to indicate whether the user was authenticated using Appian's native MFA.

## Resolved general issues

- LCP-25925 - Critical Fixed an issue where writing to related records in a process model failed in a specific scenario.

- LCP-8591 - Medium Fixed an issue where grid user filters that utilized the now() function did not apply the current time after clicking the refresh button on the grid.

- LCP-3735 - Low Fixed an issue where occasionally grid field discovery failed, causing the grid to query extra fields and slow down performance of the grid.

## Resolved accessibility issues

- LCP-15243 - Critical Fixed an issue where the file upload component was not correctly interpreted by screen readers.

- LCP-5483 - Medium Fixed an issue where some options in a long dropdown and pickers were not available to all users at high zoom levels.

- LCP-21752 - Low Added semantic content section definition to box and section layouts to assist in screen reader navigation and make content structure easier to understand for non-sighted users.

- LCP-13926 - Low Fixed an issue where some error dialogs were missing a programmatic label.

- LCP-5587 - Low Fixed an issue where the search input within dropdowns was missing a programmatic label.

- LCP-5588 - Low Added "country" as an additional supported value for the text field input purpose parameter.

## Behavior changes

This section describes behavior changes in Appian 25.4 that impact how you previously used or interacted with an existing feature, functionality, or the platform in an earlier version. This includes any changes that require you to modify your application after upgrading to Appian 25.4.

### Update plug-ins with modernized file system APIs

In 23.2, we introduced the following new APIs for file storage and retrieval.

To make use of autoscaled processes and upcoming features, you must use the supported APIs below. Plug-ins using deprecated APIs will block feature use.

- getInputStream()

- getOutputStream()

- write(InputStream inputStream)

- accessAsReadOnlyFile()

- getDocumentInputStream(long id_)

- getDocumentInputStream(long[] ids_)

- uploadDocument(Document doc, Integer unique)

- copyContents()

Update all AppMarket plug-ins in use via the Admin Console to their latest version. For private plug-ins, update deprecated APIs and submit a new plug-in version for the required deployment approval for Appian Cloud.

### Application plans from Composer no longer export or import with applications

To ensure the most consistent and reliable experience, application plans are no longer imported or exported with applications or packages.

## Evolutions

The following functions, components, or smart services have newer, improved versions in this release. Existing, old versions in your applications will continue to function normally, but will be renamed on upgrade to indicate that they are older versions.

### Read-only grids and a!queryRecordType()

We've evolved the read-only grid component and the a!queryRecordType() function to support new and improved similarity scores for smart search .

To make use of this evolved functionality, you must use the latest version of these functions and replace any existing similarity scores with ones that fit in the new numerical range .

Existing, old versions of these functions in your applications will continue to function normally, but will be renamed on upgrade to indicate that they are older versions. As always, make sure you are using the right version of the docs for your version of Appian. See Function and Component Versions for more information.

### Tempo reports

As part of making Process HQ reports deployable , we've renamed existing report objects to Tempo reports to more accurately capture their purpose. Existing versions of Tempo reports will continue to function normally.

## Removals

The features listed below have been removed from Appian and can no longer be used.

### Appian now requires Kubernetes

Self-managed Appian environments now run exclusively in containers, managed by Kubernetes. Traditional installation directly on servers or inside virtual machines is no longer available. When upgrading a self-managed environment to Appian 25.4, you must either convert to a Kubernetes-based installation or transition to Appian Cloud.

To provide you with a variety of options, Appian runs on OpenShift, Azure AKS, Amazon EKS, Google GKE, or your local or collocated "bare metal" Kubernetes cluster.

To help you with this transition, check out our migration toolkit . If you are interested in migrating to Appian Cloud, where you would no longer be responsible for managing your Appian instances or supporting infrastructure, reach out to your account executive for more information.

### Quick Apps Designer removed—build apps faster with Appian Composer

The Quick Apps Designer, deprecated in Appian 25.2 , has been removed. Applications created using quick apps will continue to function, and you can use a more powerful and intuitive way to build new applications: Appian Composer .

Appian Composer lets you plan your application and leverage the full power of Appian's data fabric to automatically generate record types, interfaces, and actions, making it easy to go from a great idea to a robust, fully-functional application.

## Feedback


---

## Appian 26.1 — synced 2026-08-16

Source: https://docs.appian.com/suite/help/26.1/Appian_Release_Notes.html

# Appian Release Notes

Share via

LinkedIn

Reddit

Email

Copy Link

Print

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

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Process complex documents using AI agents

Version : 26.7

Expand what your AI agents can see and understand with powerful new document extraction capabilities. AI agents now natively process visually complex files —like organizational charts, spreadsheets, and scanned forms—without the need for custom-built tools.

### Rapidly test chat agents

Version : 26.7

Test and refine your chat agents faster with new testing tools and flexible visual styling. The Build tab now includes a dedicated test console where you can send messages, stream responses, and inspect full chat agent timelines without needing to create an interface.

A new STOP button lets you interrupt active responses instantly in both the test console during development and in production a!agentChatField() interfaces, so end users can halt responses too.

Together, these enhancements make it easier to debug chat agents and deliver sleek, modern chat experiences to your users.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Customize chat field styling with precision

Version : 26.7

The a!agentChatField() component now enables you to take full visual control over your chat interfaces with new shape and showBorder parameters. These parameters let you quickly configure the shape of container corners, as well as show or hide outer borders. Now you can deliver more tailored conversational experiences to your users.

## AI governance

### Expand Your AI Options with GPT 5.4 and 5.5

Version : 26.7

When you choose Appian as your cloud provider, you can now use GPT 5.4 and 5.5 to power AI experiences in Appian. These highly capable reasoning models serve as reliable alternatives to Anthropic models for your generative AI skills and a!genAiModels() function. Built on a secure foundation, this approach easily meets both strict public sector compliance and regional data residency requirements.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Streamline model management with automatic routing

Version : 26.7

Protect automated processes from model deprecations with the new Auto option for AI skills . It dynamically routes executions to the best available Appian-recommended model—so your workflows keep running smoothly as models evolve, with no manual intervention required.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

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

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

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

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

## Process HQ

### Unify your dashboard view with date filters and saved defaults

Version : 26.7

Comparing data across your dashboard just got easier. In addition to dataset-based reports, you can now apply dashboard date filters to process KPIs and process-based reports .

Now, users can select a custom date range, and every item on the dashboard will reflect the same time period at a glance. You can also set default filter values so viewers see a meaningful starting point the moment they open your dashboard.

Together, these updates give you more control over your dashboard experience and help your business users get to insights faster.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Focus your process calculations with a working schedule

Version : 26.7

When you're monitoring SLA compliance or optimizing your business process , you need your duration calculations to be as accurate as possible. We're adding the ability to exclude weekends from duration calculations, so the time spent on each task reflects your organization's working hours.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

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

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### More flexible tab layouts with vertical orientation, async loading, and new tab widths

Version : 26.7

Designing secondary navigation for your interfaces just got a whole lot faster with new vertical orientation for tab layouts ! Instead of manually building vertical navigation from scratch, you can now effortlessly build it in seconds.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

Plus, you can now choose to load tabs asynchronously in the background, so data-heavy tabs don't slow down the initial page load.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

And, to give you even more flexibility, we've also added the ability to distribute horizontal tabs evenly across the tab bar.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

With these robust new styling options, you can quickly craft sleek, modern interfaces that align with your brand.

### Design polished interfaces with expanded styling controls

Version : 26.7

Build beautiful, brand-aligned applications with more precision than ever. We're giving you more control over the styling of some of our most popular components, allowing you to effortlessly design user experiences perfectly tailored to your brand.

Establish a clear visual hierarchy and match your organization's exact typography guidelines using our new font weight options. You now have more granular control over the font weight of rich text , with the addition of light and semi-bold font weights. We're also making box and section layouts more flexible by giving you control over the label font weight.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

Additionally, you can quickly add emphasis to box and card layouts by adjusting the border thickness, or draw the user's eye by configuring the border color of box layouts.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Accelerate and streamline your interface testing workflow

Version : 26.7

Now, there's a simpler way to configure test values for rule inputs in interfaces. You can easily save test values as a new or existing test scenario without navigating to the Manage Test Scenarios screen. This seamless experience eliminates context switching, allowing you to test and refine your interfaces without breaking your flow.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Enhanced legibility for the signature component

Version : 26.7

We've made the pen stroke in the signature component more prominent to ensure that all signatures are crisp and easy to read. Now, your users can verify signed documents more quickly.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

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

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

## Administration

### Capture trace IDs instantly with Interaction Diagnostics

Version : 26.7

We've made it much easier to troubleshoot slow-loading front-end design objects, removing the need to use your browser's developer tools. With Interaction Diagnostics , any authenticated user can capture diagnostic trace information (including trace ID, timestamp, duration, and response code) with a single click from the navigation menu.

Once captured, the diagnostic modal displays all relevant telemetry in a single view. Click Copy to clipboard to easily share the information with your support team or use it to investigate directly in Trace Explorer .

### Securely connect to self-hosted resources with Cloud Secure Link

Version : 26.7

We're introducing Cloud Secure Link to provide private, zero-trust connectivity to your self-hosted databases and APIs. No need to open inbound firewall ports! Simply deploy our lightweight, containerized client within your network to establish an mTLS-encrypted reverse SSH tunnel back to Appian Cloud. Then, easily manage your connections right from the Admin Console . With Cloud Secure Link, you can connect to any cloud service provider or on-premises architecture while maintaining absolute network isolation.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Pre-configure cross-region connections for optimized disaster recovery

Version : 26.7

Appian Cloud now supports cross-region PrivateLink for Enhanced Business Continuity. In cooperation with Appian Support, you'll be able to pre-configure cross-region PrivateLink connections in your secondary Appian Cloud region ahead of time. In the event of a regional failover, your inbound and outbound integrations can smoothly transition without requiring you to manually update hostnames or reconfigure your endpoints. Experience faster recovery times and complete peace of mind knowing your critical business operations remain connected and uninterrupted.

### Tailor the sign-out experience for your users

Version : 26.7

Keep your users in the flow of their work, even after their session ends. You can now configure Appian to automatically return users to their last visited page when they sign back in, allowing them to seamlessly resume their work without losing valuable context. This new behavior will apply by default to new environments; existing environments will need to manually enable this in the Admin Console .

To further unify your app for users, you can also replace the default "Return to Appian" text on the sign-out page with custom phrasing to match your organization's identity.

Tailor these simple authentication settings to provide a polished experience that helps everyone work more efficiently.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

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

## Feedback


---

## Appian 26.3 — synced 2026-08-16

Source: https://docs.appian.com/suite/help/26.3/Appian_Release_Notes.html

# Appian Release Notes

Share via

LinkedIn

Reddit

Email

Copy Link

Print

26.3 Product Webinar

Join our Appian marketing team and other Appian experts as they dig into highlights from the 26.3 release. You can also checkout our Release Showcase course on Academy Online to take a deeper dive into the latest features.

Join our Appian marketing team and other Appian experts as they dig into highlights from the 26.3 release. You can also checkout our Release Showcase course on Academy Online to take a deeper dive into the latest features.

Access new features and improvements every month on Appian Cloud

## Release Highlights

### Sync your largest datasets without row limits

Version : 26.3

We're officially removing the row limit for synced record types so you can build apps using your largest datasets. Whether you're working with comprehensive enterprise tables or years of historical data, you can sync as much information as your site's capacity allows . This gives you the complete flexibility to build mission-critical applications, knowing they can scale based on your needs.

### Relate and query across synced and unsynced data

Version : 26.2

You can now leverage Appian's most powerful data fabric features —including record-level security, relationships, and custom record fields—on unsynced record types .

When you create new record types that connect directly to a MariaDB or MySQL database, you can immediately leverage these capabilities and run federated queries across your enterprise data sources. To accelerate development, you can now generate multiple record types from your existing database tables.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

We've also made your development experience more flexible by allowing you to seamlessly switch your data access method as your application requirements evolve. Whether you choose to sync your data or query it directly, you can now build robust, data-driven applications with little to no rework.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Match your brand's unique style with CSS profiles

Version : 26.3

Ensure your applications look and feel like your brand through the flexibility of CSS profiles . This advanced branding capability in the Admin Console gives you more control over the appearance of interfaces, allowing you to configure colors, borders, headings, tooltips, and more. By mapping your organization's specific design guidelines directly to the CSS profile properties , you can easily standardize your look across all sites and portals or create unique, tailored styles for different user experiences.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Enhanced flexibility and faster innovation with Appian Cloud's new release cadence

Version: 26.1

We are excited to announce that, starting with 26.1, you can now upgrade Appian each month!

Monthly releases give you the innovations you need, when you need them, while maintaining the stability you rely on:

- Faster Access to New Features : You'll receive fully tested and supported features—every month instead of every quarter. This means shorter time-to-value for your applications.

- Greater Upgrade Flexibility : While we're offering more upgrade options, we aren't requiring you to upgrade more often. You can choose your upgrade cadence, allowing you to align upgrades with your own operational schedule.

- Easier Change Management : Smaller, more frequent releases make it easier for your teams to learn about new Appian features. Rather than having to train your teams on a quarter's worth of features, you can introduce them in smaller increments.

- Predictability Maintained : The four quarterly releases (ending with .3, .6, .9, and .12) will continue to be supported for a period of six months.

As always, we are committed to providing clear release notes, documentation, and support for every release to ensure your upgrade path is smooth and successful.

Monthly releases are available for Cloud customers only. To get started, open a support case on MyAppian .

## AI agent design and development

### Orchestrate multiple AI agents

Version: 26.1

You can now build modular, specialized AI agents as tools that collaborate directly with each other to solve complex problems. To streamline your design experience, we've removed the requirement to wrap these AI agents in process models. This empowers you to create robust AI agent interactions that are faster and more intuitive to maintain.

### Accelerate AI agent testing with expressions

Version: 26.1

We've streamlined your AI agent testing by bringing the power of expressions to the Test tab . Now, you can use familiar expressions to define complex inputs like record types, CDTs, and maps. By combining the power of expressions and complex inputs, you can now simulate more realistic scenarios and build robust, reusable test cases.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Empower your AI agents with support for arrays

Version: 26.2

Empower your AI agents to handle complex data at scale by passing arrays of documents, records, or text strings directly into Agent Studio. You can now use arrays for both input and output variables, eliminating the need for manual looping or complex parsing. This change simplifies development and reduces AI action consumption.

### Cancel AI agents instantly

Version: 26.1

Prototyping AI agents in Agent Studio is now quicker and more cost-effective. You can stop faulty executions in their tracks by immediately canceling a running agent . Instead of waiting for a process to fail, prevent wasted actions and iterate on your designs in an instant.

### Quickly render polished markdown in Agent Studio

Version: 26.2

We've introduced markdown rendering to Agent Studio to make your AI agent development experience more visual and intuitive. Your raw markdown in the Goals and Instructions field now automatically converts into sleek headers and readable bulleted list of instructions. This more intuitive formatting helps you to quickly understand your results and iterate on your AI agents faster than ever.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Gain full visibility into AI agent activity

Version: 26.1

We're helping you more effectively manage your AI strategy with comprehensive logging and metrics for AI agents. We've integrated AI agent runs into standard system logs so that you can easily audit interactions and maintain security compliance. And, new accurate AI action metering helps you to keep track of specific costs and optimize resource usage across your entire organization.

### Streamline AI agent development in the Build tab

Version: 26.2

Accelerate your AI agent development with the new unified Build tab in Agent Studio .

We've consolidated configuration and testing into a single, split-pane view. Now, you can view AI agent configurations and real-time performance side-by-side for a faster, more intuitive development experience.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

## AI skills

### Boost accuracy with extended thinking

Version: 26.2

Tackle complex automation with greater precision using extended thinking—now available in the generative AI Skill ! This enables models to reason through intricate logic for complex tasks before responding, which significantly reduces errors. With the new Model Thinking output you gain full visibility into the model's reasoning to build greater trust in your AI-driven processes.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

## AI governance

### Run AI skills with Amazon Nova 2 Lite

Version : 26.3

Appian AI skills now support Amazon Nova 2 Lite, giving you a fast and capable alternative to Anthropic models. Whether you're navigating supply chain compliance requirements or simply want more flexibility in how you power your AI features, Nova 2 Lite's text and vision capabilities give you a reliable, high-performing alternative right out of the box.

Support for Amazon Nova 2 Lite was released in Appian 26.4 and is also available in Appian 26.3.

### Give your organization full control over where and how Appian AI runs

Version: 26.2

Appian now supports using your own AWS account with Amazon Bedrock, allowing generative AI requests to execute directly within your organization's AWS environment. With a new configuration in the Admin Console and the existing option to select your own models, it's easy to apply your organization's security and governance policies.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Run complex AI skills in autoscaled processes

Version: 26.1

The Execute Generative AI Skill smart service's long-running mode is now available for autoscaled processes . This update lets you run in-depth or large AI tasks while also leveraging the speed and power of autoscale.

### Trace generative AI executions with model IDs

Version: 26.1

Gain deeper insights into your AI operations with the addition of model IDs to AI Audit Logs . This new capability identifies the specific model used for every generative AI execution, helping you more effectively debug and monitor your processes for compliance.

## AI Copilot for developers

### Generate record type descriptions with AI Copilot

Version: 26.1

Record type descriptions allow business users, developers, and AI to better understand your data. Now, you can use AI Copilot to generate record type descriptions and quickly provide a summary of your data.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

## AI Copilot for business users

### Deliver rich and responsive chat experiences

Version: 26.1

We've enhanced the a!chatField() component to help you deliver more natural, engaging, and professional AI conversations. Users now receive real-time streaming responses that appear instantly as they are generated, while developers gain greater design control with rich text support and customizable background styling. AI responses appear as professional, structured content instead of unformatted text, creating a more intuitive experience for your users.

We've also improved the a!callLanguageModel() function so it's easier to support long-running conversations. These updates allow you to create polished, conversational interfaces that fit perfectly into any layout.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

## RPA

Version : 26.2

Robotic process automation simplifies how you build, manage, and scale digital workers to handle repetitive tasks across systems. By automating routine processes, your teams can focus on higher-value work that drives innovation and efficiency.

### More reliable automated login

We've improved stability during logoff, ensuring your enterprise automation runs smoothly without unexpected service disruptions. This improvement is especially valuable for organizations running large-scale automation programs that rely on consistent automated login functionality.

### Strengthened security and operational reliability

We made the following improvements to strengthen your RPA environment:

- Seamless User Experience : Resolved issues where robotic tasks failed to import or display correctly in Appian Designer, and enhanced smart service retry mechanisms to automatically handle temporary issues, reducing manual intervention.

- Improved Reliability : We've enhanced backend server startup processes to ensure consistent system availability.

- Enhanced Security : Updated internal components and infrastructure to protect your sensitive data.

### Intelligent RPA prerequisite checks

RPA now includes more built-in prerequisite checks that verify critical system dependencies, such as database connectivity, before a process begins. By confirming your environment is ready for action, Appian prevents unnecessary interruptions and guarantees that your automations execute under optimal conditions.

### Quickly resume robotic tasks after closing popups

We've improved the reliability of robotic tasks when working with multiple browser windows. Robotic tasks now smoothly transition back to the primary browser window after closing secondary popups. This update ensures your workflows maintain momentum, providing a more robust and dependable execution for your complex processes.

## Data fabric

### Fully integrate external documents into your data fabric and apps

Version : 26.3

We've made it easier than ever to work with critical business documents, regardless of where they live. Now, you can use record types to integrate external documents into your applications just as easily as documents stored in Appian.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

Configuration is simple—just add an integration to your record type that tells Appian how to retrieve a document. Then, you can instantly display and download external documents using components like the Document Viewer , Document Image , and Document Download Link . You can even incorporate external files into your workflows, automations, and expressions using the Return External Document smart service .

And, you can be confident that your documents are secured using the same security configured on your record types.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Sync data from tables with composite keys

Version : 26.3

You can now create synced record types for any database tables that use a composite primary key, giving you the flexibility to work with your existing data models exactly as they are. Once synced, you can immediately start querying and writing data using the same functions you already know and love, like a!queryRecordByIdentifier , a!writeRecords , and a!syncRecords .

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Use database views in your data fabric

Version : 26.2

You can now use database views as the source for any synced or unsynced record type! This allows you to easily incorporate data from highly tuned views or leverage pre-calculated data for your most complex business cases. With this added flexibility, you can unify your most sophisticated data sources in your data fabric.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Accelerate your data fabric setup by generating record types

Version : 26.3

Building your data fabric just got even faster! You can now generate multiple record types from database tables and views in just a few clicks—including tables with composite primary keys . To save you time, we'll automatically relate your record types based on existing foreign keys and secure them using your application's groups.

With your newly generated record types, you can immediately leverage powerful features like Process HQ and the Data Fabric Chatbot to get more from your data. This streamlined experience helps you dramatically accelerate your initial app setup and makes it easier than ever to modernize your existing applications.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Build smarter applications with dynamic record metadata

Version : 26.3

Unlock the full potential of your data with the newly expanded a!recordTypeProperties() function ! You can programmatically discover record types and their metadata—like their fields and relationships, and now, their record views and actions.

You can even use AI-powered search to find the most relevant record types for your users. You can control how close a match you need for your AI-powered searches, ensuring your users always have the right data at their fingertips.

### Add more record type relationships

Version : 26.3

We're giving you the flexibility to unify even more of your enterprise data by allowing you to add as many relationships to a record type as you need—there is no limit!

### Find exactly what you need with full-text search on documents

Version : 26.3

Smart search now gives you the power to choose between semantic and lexical search, making it easier than ever to find the right information. We've added lexical search capabilities to smart search so you can perform full-text searches across document contents and extra-long text fields—perfect for finding a specific phrase in a PDF or an exact value in a long description.

Plus, with support for up to 5,000 matches, you can feel confident that you're seeing all of the relevant search results.

### Find more information faster with enhanced smart search

Version : 26.2

We're committed to scaling smart search alongside your data fabric. This release, we've increased the number of rows you can search in each record type to:

- 10 million rows of text.

- 3.75 million rows of extra long text.

- 325,000 rows of documents.

We've also optimized indexing performance to be up to 11x faster and expanded our smart search results to show up to 500 matches.

Plus, we've extended our search capabilities to scanned PDFs . With these powerful enhancements, users can find exactly what they need, no matter how much data you have.

### Easily discover record types and their metadata

Version : 26.1

We're helping you build smarter, more flexible data fabric-powered applications with the new a!recordTypeProperties() function. This function returns record types and their related properties, like their source, fields, and relationships, so that you can easily build dynamic interfaces and queries based on your data structure.

This function also lets you use AI-powered search to discover all of the relevant record types that you need, even if you're not searching by the exact search term. With this new function, you can empower your users and AI agents to find the right data faster than ever.

### Capture AI agent activity in your record events

Version: 26.3

You can use record events to track what happens in your apps and which users or automations are taking action on your records. This release, we're building on this to give you more flexibility when capturing automated events.

You can now select the new AI Agent automation type in the Write Records smart service nodes to capture actions performed by AI agents . This new automation type allows you to easily attribute completed events to AI agents, AI skills , and other types of automation, helping you gain more detailed insight into the impact of automation on your key business processes.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Take control of your full sync schedule

Version : 26.1

Keeping your synced data fresh just got more flexible. Now, you can schedule full syncs to run either daily or weekly. Simply choose the frequency that best matches your business needs to ensure your users always see the latest information.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

## Process modeling and autoscale

### Remediate errors faster with bulk node restarts

Version : 26.3

In 26.2, we made managing autoscale workloads easier with the ability to restart or skip errored process nodes in bulk. Instead of addressing issues one by one, you can use the error dashboard to select and remediate thousands of nodes simultaneously, ensuring your mission-critical processes stay on track. By quickly filtering on specific errors, you can get your operations back up and running with just a few clicks.

In 26.3, the process history for autoscaled processes now shows if the process was canceled, where the process flow stopped, and who canceled the process.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### See autoscale compatibility in Appian Designer

Version: 26.3

Curious if your process models are ready to make use of Appian's high-throughput capabilities ? Starting this release, we now automatically check if a process model can be updated when your environment has autoscale enabled. If it is, an icon is added to that model in the object list. When you're ready to update, just open the process model, and select Use process autoscaling in the process properties.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Effortlessly convert subprocesses to the Start Process smart service

Version: 26.1

We're making it simpler to modernize your process models, adopt best practices for standard and autoscaled processes, and simplify your migration to autoscale. The process modeler now automatically detects subprocess nodes that are eligible for conversion and, with just a click, swaps them with the Start Process smart service . To get started, just open a process model with subprocess nodes and use the design guidance to convert those nodes.

### Add start forms to autoscaled processes

Version: 26.1

To help you run more of your existing work with autoscale , we're excited to announce support for process start forms . Now, record actions and start process links can call an autoscaled process, letting users see the configured start form and provide data for the new process instance.

### Configure recipients for process alert emails

Version: 26.1

To better protect your user's personal information, we're enhancing the security of process alert emails. Starting this release, all recipients will be placed in the Bcc field by default, preventing accidental email address exposure. You can choose to put recipients in the To field by changing this setting in the Admin Console .

### Use more smart services in autoscaled processes

Version: 26.3

It's now easier than ever to migrate your existing process models to use autoscale. We've expanded support by adding smart services for data and document management:

- Delete from Data Store Entities Smart Service

- Query Database Smart Service

- Sync Records Smart Service

- Delete Records smart service (all versions)

- Create Folder smart service

- Delete Document smart service

- Send Email smart service

And, autoscaled processes can now use the Execute Generative AI Skill smart service in long-running mode, letting you run complex or large tasks with generative AI models.

## Process HQ

### Act faster on insights with the redesigned detail page

Version: 26.3

This release, we've redesigned the insight details page to help you understand exactly what each insight means, why it's important, and what you can do about it.

You'll see AI-generated insight summaries right at the top of the page, followed by visualizations that help show impact at a glance. We've also added a new section that highlights recommended actions, which can be copied and immediately used to take action with Appian Composer .

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

With this new streamlined experience, you can move from discovering a bottleneck to fixing it in record time.

### Get instant visibility into your data

Version : 26.3

We've enhanced the Data Catalog to give you instant visibility into every dataset, helping you find the perfect data for your reports faster. Now, you can click any dataset to quickly review its fields, freshness, and even preview the data, so you can pick the right information and stop guessing before you even start building.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

We've also modernized the Data Governance page with a new card-based layout, making it easier for data governors to manage dataset visibility and data stewards in Process HQ. These improvements ensure your organization has the clarity it needs to quickly turn data into actionable insights.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Get more out of your KPI reports with target visualization

Version: 26.3

We've added new options to allow you to customize the appearance of your KPI reports . You can now configure a target value and progress bar to highlight how well the KPI is performing and help users contextualize the KPI's current value.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Compare KPI performance against a baseline

Version: 26.3

We're introducing baselines to KPIs to make it easier to evaluate performance at a glance. You can set a baseline value for your KPIs that represents how long it took to complete a case , activity , or sequence in the past. The baseline appears directly on the chart so users can easily compare it to the KPI's current performance.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Track indirect sequences with duration KPIs

Version: 26.3

We're updating duration KPIs to support indirect sequences . This allows you to track duration and SLA compliance between any two parts of a process, regardless of how many steps are in between.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

With this update, we're giving you more power to measure the success of your processes and track the indicators that are most relevant to your business.

### Add more items and filters to your dashboards

Version: 26.3

Over the past three releases, we've introduced and enhanced interactive filters to dashboards in Process HQ. You can now add up to 10 custom filters that allow your users to filter all reports and process KPIs on a dashboard at once.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

And, dashboards now support up to 20 reports and process KPIs . You can even create a new report while you're building a dashboard, so you can add more details without ever leaving the page.

With these enhancements, your dashboards can tell a broader story about your enterprise data, and your users can explore more data with a single dashboard.

### Generate actionable application improvements with AI-powered insights

Version : 26.2

We've supercharged our insight summaries to help you optimize your applications. These improved insights summaries provide deeper process context and a specialized understanding of Appian objects. This means you get highly specific recommendations that bridge the gap between business needs and technical implementation.

### Customize your heatmap charts with diverging color palettes

Version : 26.2

Last release, we introduced heatmap charts for reports to help you easily visualize patterns, correlations, and intensity within large datasets. Now, you can customize your heatmaps with two new color palettes that are designed to highlight deviations in your chart's data.

This added flexibility gives you even more ways to build powerful reports and understand your business data at a glance.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Visualize KPI performance with reference lines

Version : 26.2

KPIs are an invaluable tool for tracking your process performance. With this release, you can add reference lines to your KPI visualizations, allowing you to add targets, thresholds, or benchmarks directly on your charts. These visual cues make it easier to see at a glance exactly how your process is performing against your goals.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

You can also specify whether your KPI value should be higher or lower, so KPI visualizations and alerts align with your business goals.

With these updates, we're giving you more control over your KPIs so you can quickly assess your process performance.

### Easily monitor reports and dashboards with versioning

Version : 26.2

This release, we're adding versioning support for report and dashboard objects so developers can easily review, revert, and compare object versions. With this update, monitoring changes to reports and dashboards in your app is easier than ever.

### Access process insights capabilities in more regions

Version : 26.2

We're excited to announce that we're expanding the regional availability of process insights to our customers in the Japan (Osaka) region.

### Find the most impactful process improvements faster

Version : 26.1

Process HQ now points out valuable process improvements the moment you open an average duration KPI . Right in the KPI details, we've added a Suggested Insights feed that shows you the most relevant characteristics of your process data ranked by impact. Plus, simple but powerful charts help you assess each suggested insight at a glance.

With these suggestions at your fingertips, you'll spend less time combing through your data and more time making valuable improvements to your business processes.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Create new report visualizations with heatmaps

Version : 26.1

You can now create heatmap charts in your reports to visualize patterns, correlations, and intensity within large datasets. Just like other chart types, you can customize the data and appearance of your heatmap chart, including interactive elements like quick filters and drilldown reports.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

With this new chart type, you can identify relationships between variables in your business data.

### Create richer reports with new chart display options

Version : 26.1

We've upgraded Process HQ reports with new configuration options. These new options allow you to add reference lines to your charts, show or hide a chart legend, show data labels and tooltips, and customize chart axis titles.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Accelerate report and dashboard development

Version : 26.1

We're continuing our commitment to a unified development experience for reports and dashboards .

You can now create reports and dashboards just like other design objects, making it even simpler to integrate Process HQ deliverables into application design.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

Then, when you're ready to deploy, you can directly review differences in reports and dashboards across environments, accelerating iterative development.

Now more than ever, developers can leverage the power of Process HQ for business users without any change to your existing application lifecycle.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Add display names to report fields

Version : 26.1

Make your reports easier to read and understand by adding display names to your report fields . Now, while creating or editing your reports, you can give fields readable, business-friendly names.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

## Sites and portals

### Hide the user menu in sites for more flexibility

Version : 26.2

Environments that use single sign-on and logout can now hide the entire user menu in sites. This configuration gives you more control over your site design by removing the profile image and user menu from your site header, allowing you to create a more tailored experience for your users.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Simplify site and portal development with object versioning

Version : 26.1

We're bringing a more robust experience to developing and managing site and portal objects with the introduction of versioning .

Similar to many other design objects, you can now view a history of all saved versions, compare two versions side-by-side, and easily revert the site object to any previously saved version. This makes it easier to track changes and collaborate with more confidence.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Enhance your site with Process HQ dashboards

Version : 26.1

You can now add Process HQ dashboards as pages in your Appian Site , so your users can easily access the business data they need right where they do their day-to-day work.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

And, to ensure a cohesive look across your entire site, it's easy to customize the page's appearance with light or dark themes, and even apply your organization's unique branding!

## Interfaces

### Seamlessly organize interfaces with the new tab layout

Version : 26.1

Organizing complex content in your interfaces just got a whole lot simpler. We're excited to introduce the new tab layout , which lets you organize your content into tabs that users can nimbly navigate between.

Configuring the tabs is a breeze—allowing you to effortlessly add icons, custom highlight colors, and tailored padding to match your application's branding. We handle the navigation logic for you, allowing you to create a seamless, intuitive experience for your users in just a few clicks.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Effortlessly test interfaces with saved test scenarios

Version : 26.1

You can now define, save, and run multiple sets of rule input values as test scenarios in interface objects. Use test scenarios to instantly switch between different data configurations and view precise load times, making it easy to verify everything from happy paths to edge cases.

And testing is even more flexible with improvements to rule input value fields in both interface objects and expression rules. Not only are these fields now expandable, but we've also significantly increased the character limit more than tenfold, meaning you can easily manage and view large values for your most complex logic.

This streamlined testing experience makes it easier than ever to validate your logic and deliver robust applications with confidence.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Simplify capturing true or false answers with two new components

Version : 26.2

We've added two new ways for you to capture true or false values in your interfaces.

In 26.1, we introduced the boolean checkbox component, making it easy to configure an input field to capture a true or false response. This new component is perfect for common tasks like accepting terms and conditions or confirming a choice.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

Building on that foundation, the 26.2 release introduced the toggle component for even more flexibility, providing a sleek alternative for actions that take effect right away, such as hiding content or turning on settings.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

By choosing the right tool for the job—checkboxes for forms and toggles for state changes—you can build more intuitive and responsive interfaces in just a few clicks.

### Optimize grid performance with simplified paging controls

Version : 26.3

We've optimized read-only grids and record lists by hiding the total row count by default, significantly boosting your loading speeds as your data scales. While this provides a faster and more streamlined experience, you can still display the total row count when needed using the new pagingControls parameter . To take advantage of these performance gains, simply update your record types to hide the total row count or start using the latest version of the read-only grid.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Design sleek grids with new selection styles

Version : 26.3

You can now build sleeker, user-friendly grids with two new grid selection styles . The new Subtle Highlight provides a softer highlight of your selected rows, while the Checkbox and Subtle Highlight option offers a modern feel that makes it instantly clear which rows are selectable.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Create flexible, nested side-by-side layouts

Version : 26.1

We're allowing you to build more complex designs with ease with enhancements to the side by side layout . Now you can nest side by side layouts and include multiple components within a single side by side item , allowing you to easily stack and arrange components next to each other with perfect alignment. Plus, we've simplified the design mode experience to make configuring these components more intuitive.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Control refresh behavior in the styled text editor

Version : 26.3

Build more dynamic interfaces with the new refreshAfter parameter in the styled text editor . To precisely control how your interfaces react to user input, you can now trigger interface evaluations after every keypress, rather than only when a user clicks away from the styled text editor.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Build and debug interfaces swiftly with enhancements to the interface object

Version : 26.1

We've supercharged your interface development with a collection of productivity enhancements designed to streamline your daily workflow. We'll automatically open interface objects in design or expression mode based on what mode you were last in when you last closed any interface.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

Debugging interface, expression rule, and web API objects is now a breeze with clickable error messages that take you directly to the exact line of code.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

Navigating nested components is quicker with a redesigned component selector that lets you easily select the parent component.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

We've also increased the height of the expression dialog in design mode to reduce scrolling.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

Plus, you can now see the full name of an object by simply hovering over it in the header.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

These refinements eliminate friction throughout the design process, allowing you to focus on building high-quality interfaces.

### Designing interfaces is up to 7x faster

Version : 26.3

Since the Appian 25.1 release , we've made the interface design experience up to seven times faster, allowing you to quickly build and refine your interfaces with ease. The Appian 26.1 release continued this trend by speeding up some of your most common interface design actions to help you work faster.

You'll notice that the following header interactions are now speedier and more responsive:

- Save.

- Undo and redo.

- Switch to preview and performance views.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

In Appian 26.3, we also made the following general performance improvements, which affect both the design and user experiences:

- Faster save operations : In most cases, user interactions that trigger an a!save() in a saveInto parameter are now faster.

- More efficient evaluations : Interfaces evaluate faster thanks to improvements to our underlying framework.

With these updates, your entire design and user experiences feel snappier and more fluid.

### Boosted performance for key components

Version : 26.3

Deliver a more responsive experience for your users with increased performance of popular components up to the following amounts:

You'll see the greatest performance boost on your most complex designs that have many components or highly nested components. This enhancement ensures your interfaces remain highly performant and efficient, even as your interfaces increase in complexity.

### More modern user profile images

Version : 26.3

Deliver a more personalized and professional experience with the evolved user image component that now displays stylized initials whenever a profile photo isn't available. You can also use the new backgroundColor parameter to ensure these initials always blend in with your interface design.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Design spacious layouts with a new column width

Version : 26.1

We've added a new "EXTRA_WIDE" option to the width parameter of column layout to help you easily match modern design standards and make the most of wider screens.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Sleeker shadows on card and box layouts

Version : 26.3

We've updated the appearance of shadows on card and box layouts to provide your applications with a more sleek and modern aesthetic. This update ensures your interfaces feel fresh and sophisticated without requiring any manual changes to your existing designs.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Improved contrast for the Secondary color

Version : 26.1

We've updated the Secondary color option to increase the contrast ratio. This makes it easier to see on light backgrounds and helps you apply consistent, accessible colors to a variety of components.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Automatically truncate long button labels

Version : 26.1

Buttons now truncate if the label is too wide for its container, preventing text from overflowing. Users can view the full text if a tooltip is configured.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

## Control Panel

### Empower business users with a more inclusive experience

Version : 26.1

The form and interface configuration experience in the Control Panel is now more user-friendly for keyboard users. The new keyboard mode provides an alternative configuration experience to drag-and-drop that allows business users to build and configure interfaces using only their keyboard.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

And, we've improved numerous interactive elements throughout the Control Panel to make them more inclusive, including parts of the side navigation, dialogs, and color pickers. These improvements empower a wider range of users to be a part of the design and configuration process for their business critical applications and workflows.

### Translate category and type names for the Control Panel

Version : 26.1

We've added more translation capabilities to the Control Panel workspace and object. Now, low-code developers can use translation strings for the display names and descriptions of categories and types directly from the control panel object. The translated display names and descriptions will be seen by business users in the Control Panel workspace, as well as end-users of your apps. By making it simpler to translate more key pieces of your apps, you can provide your users with a more cohesive and intuitive experience in their preferred languages.

### Case Management Studio

#### Accelerate document management with native document record type

Version : 26.2

We've refactored the Case Management Studio architecture to use Appian's out of the box document record type , dramatically increasing the speed and efficiency of your workflows. You'll notice significantly faster and more seamless interactions with documents throughout your app, such as uploading files to cases and tasks.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

And, we've created a simple, one time migration process to painlessly move your existing documents over to the new optimized architecture! Together, these architecture and migration enhancements are working together to provide a smooth transition to a more streamlined experience for both you and your users.

#### Upgrade with ease

Version : 26.2

We've streamlined the upgrade process for Case Management Studio to help you implement the latest features faster. Instead of downloading the whole solutions package to upgrade, you can now download a single, targeted delta package for each release that only contains the new and modified objects you need for your upgrade. We're also providing you with out-of-the-box scripts to automatically migrate your existing data from 2.0 in Case Management Studio tables into the upgraded architecture for 2.1. These improvements help reduce the size and scope of your upgrades, allowing you to focus on progress rather than process.

#### Accelerated task and case processing

Version : 26.2

In this release of Case Management Studio , we've optimized key process models to ensure that your business processes are quicker and more performant. Now, these processes allow critical actions like submitting cases and completing tasks to run up to 60% faster!

#### Load interfaces asynchronously

Version : 26.2

Now, your most complex Case Management Studio interfaces will feel faster and more responsive as soon as you land on the page. We've added asynchronous loading capabilities to the UIs so that your core page details and information load first, while more content-heavy components load in the background. This means that your users can start interacting with parts of an interface immediately and ensures that even your most data-rich pages are performant and scalable.

#### Fine tune sub-case completion with ease

Version : 26.2

Gain greater control of your case workflows with new sub-case configuration options in the Create Case task type . You can now decide whether a process moves forward as soon as the sub-case is created, or if it should wait until the sub-case is complete before continuing on. This flexibility allows you to design more precise workflows that better align to your specific business needs.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

## Integrations

### Authenticate to SharePoint with client certificates

Version: 26.3

We've modernized the SharePoint connected system to support the Entra ID identity platform to give you tighter security without using shared passwords. For the authorization code flow, you can now choose between client secret and the new client certificate method .

And, this new flow ensures you are ready for the retirement of Azure ACS . Just pick the new Authorization Code option to update your connected systems!

### Client credentials authentication for Salesforce connected systems

Version : 26.1

You can now authenticate your Salesforce connected systems using the OAuth 2.0 client credentials flow. This authentication type allows you to configure secure, server-to-server integrations without relying on a specific user's credentials. By adopting this Salesforce-recommended standard instead of username-password authentication , you can ensure your critical integrations run smoothly.

## Appian Mobile

### Experience full-screen immersion with edge-to-edge display on Android devices

Version : 26.3

Give your Android users a more modern experience with edge-to-edge display in the Appian Mobile app. The app now seamlessly extends to the top and bottom of the device frame, providing a sleek user experience that looks fantastic on all devices running Android 15 and up.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### A more modern display name in the Appian Mobile menu

Version : 26.3

Instead of usernames, the Appian Mobile menu now shows the user's first and last name, adding just a touch more friendliness to the mobile experience.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

## Plug-ins

### Parameter keywords for function plug-ins

Version : 26.1

Custom function plug-ins can now opt into keyword support, enabling optional parameters and flexible ordering in the expression editor, just like Appian's out-of-the-box functions. With just a small update to your plugin manifest file you can let developers focus on building expressions that work the first time—no guesswork required!

### Enums for component and function plug-ins

Version : 26.1

Both component and function plug-ins now support enum types , allowing parameters to be configured with a fixed set of values. This unlocks auto-completion and error flagging in the expression editor, letting developers pick the right values quickly.

### Simpler configuration for component plug-ins

Version : 26.1

Component plug-ins have three new options that make it more intuitive to guide Appian developers using the component. Placeholder values automatically populate the configuration when the component is added from the palette. You can also set a parameter as required to provide immediate validation when configuring the component. Default values can be set to apply when a parameter is not configured. These options enhance developers' ability to use custom components with your helpful guidance as they work.

### Enhanced component plug-in security

Version : 26.1

For greater security, component plug-ins can execute client API backend operations using the context of the end user making the request and leverage Suite API services to simplify viewing or updating business data. And parameters used for server-side logic can also be marked as secured , safeguarding critical configuration values and strengthening overall application security.

### Improved annotations to understand plug-in data usage

Version : 26.3

It's important to understand how your plug-ins use Appian data and the effects this will have on the system. To make this easier, we are introducing annotations that show exactly what data will be read or written when you use an API. Knowing which Appian engines are used by the different parts of your plug-in helps you build with safety and scalability.

## Administration

### Deploy globally with Appian Cloud in Osaka

Version : 26.3

Host your applications closer to your users with the new Appian Cloud region in Osaka, Japan. This expansion allows you to easily meet local data residency requirements and strengthens your in-country disaster recovery strategy by pairing Osaka with Tokyo regions as part of Enhanced Business Continuity . Deliver your most important services with the confidence of in-country redundancy.

PrivateLink and VPN features are currently unavailable in this region. To learn more about existing limitations, see our Appian Cloud availability docs.

### Centralized branding management in the Admin Console

Version : 26.3

Manage your visual identity from a single, reorganized Branding page in the Admin Console. We split the original page into tabs for environment-wide General settings and Sign-In and Tempo styles. You can also find Typefaces and the new CSS Profiles here, providing one centralized location to manage all your branding options.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Streamlined data encryption with Appian-managed keys

Version : 26.3

We're expanding our encryption capabilities with Appian-managed keys, a natural upgrade to our Bring Your Own Key (BYOK) offering. Signature Success Plan customers can now have us automatically handle database encryption and transparent database encryption , removing the need to manage with your own AWS account. This seamless protection ensures your data is always encrypted at rest, giving you total peace of mind with zero administrative effort.

### Multi-factor authentication on by default for Appian users

Version : 26.1

We are committed to providing the strongest security foundation possible for your users and data. All newly created Appian environments using native authentication will now have multi-factor authentication (MFA) on by default. This change strengthens Appian's security posture, ensuring that user accounts are protected with email- or token-based authentication and reducing the risk of unauthorized access. Contact Appian Support if you want to enable MFA in an existing environment.

### Limit multiple sign-ins for SSO users

Version : 26.2

Appian already lets you limit the number of times users with Appian accounts can sign in. Starting with this release, you can also enable this setting for users authenticating with OpenID Connect (OIDC) , SAML , or PIEE . Just like with Appian accounts, you can configure the maximum number of concurrent sign-ins, so you can meet your organization's security requirements and comply with security frameworks.

### New authentication options for DevOps APIs

Version : 26.1

In this release, we enhanced security for system-to-system communication with new authentication options.

Now, administrators can configure mutual TLS (mTLS) authentication for the Connected System Management and Deployment APIs. This enables two-way authentication for all inbound requests, helping you meet compliance requirements for external systems that update connected system credentials.

Additionally, requests to the Deployment API can now use OAuth 2.0 client credential authentication as an alternative to API keys. With these enhancements, we're helping DevOps teams to deploy and update applications with greater security.

### Support new locales for 26.1

Version : 26.1

We're excited to announce that Appian now supports these additional locales, so you can provide your users with a best-in-class experience in their preferred language and locality.

You can find these newly added locales in the Internationalization section in the Admin Console :

- Danish

- Indonesian

- Slovenian

- Ukrainian

- Vietnamese

- Welsh

### Support new locales for 26.2

Version : 26.2

We're excited to announce that Appian now supports these additional locales, so you can provide your users with a best-in-class experience in their preferred language and locality.

You can find these newly added locales in the Internationalization section in the Admin Console :

- Portuguese (Portugal)

- Spanish (Mexico)

- Dutch (Belgium)

- French (Belgium)

- Catalan

### Manage mail server certificates with zero downtime

Version: 26.1

You can now upload and select client certificates for your mail server directly from the Admin Console . Even better? There’s no need for an environment restart. With centralized certificate management, you can secure your email communications and keep your business processes running smoothly.

### Appian on Kubernetes Migration Tool enhancements

Version : 26.1

The Appian on Kubernetes Migration Tool has been expanded to give you better control and understanding of your migration journey. The expansion includes two new abilities. You can now exclude specific data from the tool's process, allowing you to choose how to transfer it. And, you can now run the tool in a draft mode, which creates an Appian YAML file configured for your Appian environment but doesn't execute the entire process.

Also, we've added options that make migrating self-managed Appian from Windows or Linux into Appian Cloud much easier. To learn more, contact your Account Executive.

### Easily view user UUIDs

Version : 26.1

We're continuing our mission to make it easier for low-code developers to find the information they need faster. In 25.4, we introduced object UUIDs to the Properties dialog . In this release, we've added user UUIDs directly to the User Properties dialog, the Users view in Designer , and the Admin Console . Now, you quickly reference the UUIDs from more convenient locations with no extra time or clicks necessary.

### Quickly deploy plug-ins in bulk

Version : 26.3

We're excited to streamline plug-in management for your environment and reduce repetitive work with bulk plug-in deployment. You can now select and install all the plug-ins you need in a single action! This removes the friction of deploying one at a time, giving you a faster and more reliable way to equip your environment with the right tools.

## General resolved issues

### 26.1 General resolved issues

Version: 26.1

- IOS-10839 - High Fixed an issue where memory was leaking during file upload in the iOS mobile app.

- IOS-10846 - High Fixed an issue where the list of offline task ids that the user has submitted wasn't properly updated after a user manually signs out and deletes pending offline forms in the iOS mobile app.

- DR-8479 - High Fixed an issue where the list of offline task ids that the user has submitted wasn't properly updated after a user manually signs out and deletes pending offline forms in the Android mobile app.

- LCP-21981 - Low Fixed an issue where using the Start Process smart service in synchronous mode would incorrectly add an error to the authorization audit log file.

- EA-5885 - Low Fixed an issue where the width parameter of side by side item didn't validate values when the item parameter was null. Previously, invalid lowercase values like "2x" were silently treated as "AUTO" instead of returning a validation error.

### 26.2 General resolved issues

Version: 26.2

- LCP-10872 - Medium Fixed an issue that caused the sizing script to fail resulting in missing and unexpected data in the Health Check reports.

## Accessibility resolved issues

### 26.1 Accessibility resolved issues

Version: 26.1

- LCP-22999 - Medium Fixed an issue where the grid selection column was missing a header when a maximum selection value was set on the grid.

- LCP-5498 - Medium Removed redundant screen reader text in grid column headers related to sortability and sort direction.

- LCP-24064 - Low Improved accessibility of site sidebar navigation tabs.

- LCP-19396 - Low Fixed an issue where section, form, and wizard level validations were not announced in record actions dialogs.

- LCP-19364 - Low Improved duplicative dialog label announcements.

- LCP-5506 - Low Fixed an issue where visible focus was not shown on dialogs upon opening and focus was not moving to record action dialogs upon opening.

- LCP-5501  - Low Improved the keyboard navigation of menu-style record actions.

- LCP-5496  - Low Improved overall accessibility of grid column headers.

### 26.2 Accessibility resolved issues

Version: 26.2

- LCP-5493 - Low Fixed an issue where the required field indicator was identified as a graphic.

### 26.3 Accessibility resolved issues

Version : 26.3

- LCP-40209 - Medium Fixed an issue that allowed users to navigate to content behind dialogs using arrow keys.

## Behavior changes

This section describes behavior changes in Appian 26.3 that impact how you previously used or interacted with an existing feature, functionality, or the platform in an earlier version. This includes any changes that require you to modify your application after upgrading to Appian 26.3.

### Updated operator for performing semantic search

Version : 26.3

We've enhanced smart search to support both semantic and lexical search , giving you more ways to find the data you need. To reflect these new capabilities, we've introduced the "semantic search" operator to replace the generic "search" operator in your queries.

While your existing queries will continue to perform semantic searches using the "search" operator, you should begin using the new "semantic search" operator for any new queries to ensure your applications stay up to date with our latest standards.

### Updated handling of substitution values

Version : 26.3

To prevent document corruption, the following smart services now handle special characters ( & , < , > ) in substitution values before inserting them into the document:

- MS Word 2007 Doc from Template Smart Service

- Open Office Writer Doc from Template Smart Service

## Evolutions

The following components have newer, improved versions in this release. Existing, old versions in your applications will continue to function normally, but will be renamed on upgrade to indicate that they are older versions.

### Read-only grids

Version : 26.3

We've evolved the read-only grid component so that the total row count is no longer queried by default—improving overall grid performance. Now, you can choose whether to query and display the row count using the pagingControls parameter .

### User image component

Version : 26.3

We've evolved the user image component so that it displays user initials whenever a profile photo isn't available. We've also added a backgroundColor parameter so you can choose a color to display behind the initials.

## Deprecations

The features listed below are deprecated and will be removed in a future release of Appian. Do not begin using deprecated features, and transition away from any prior usage of now deprecated features. Where applicable, supported alternatives are described for each deprecation.

### Non-containerized self-managed environments

For self-managed environments, Appian 25.3 was the last non-containerized version and will continue to receive hotfixes and critical updates throughout its support period . When you're ready to update, Appian on Kubernetes is the path forward for self-managed deployments.

### Suite API

Version : 26.3

The following methods have been deprecated across all APIs.

- accessAsReadOnlyFile()

- addCommunitiesToFavorites(Long[] communityIds_) and removeCommunitiesFromFavorites(Long[] communityIds_)

- addCommunityToFavorites(Long communityId_) and removeCommunityFromFavorites(Long communityId_)

- addDocumentsToFavorites(Long[] doids_) and removeDocumentsFromFavorites(Long[] doids_)

- addDocumentToFavorites(Long doid_) and removeDocumentFromFavorites(Long doid_)

- addFoldersToFavorites(Long[] foids_) and removeFoldersFromFavorites(Long[] foids_)

- addFolderToFavorites(Long foid_) and removeFolderFromFavorites(Long foid_)

- addGroupToFavorites(Long groupId_) and removeGroupFromFavorites(Long groupId_)

- addKnowledgeCentersToFavorites(Long[] kcids_) and removeKnowledgeCentersFromFavorites(Long[] kcids_)

- addKnowledgeCenterToFavorites(Long kcid_) and removeKnowledgeCenterFromFavorites(Long kcid_)

- addProcessModelToFavorites(Long modelId_) and removeProcessModelFromFavorites(Long modelId_)

- addProcessToFavorites(Long processId_) and removeProcessFromFavorites(Long processId_)

- addTaskToFavorites(Long taskId_) and removeTaskFromFavorites(Long taskId_)

- addUserToFavorites(String username_) and removeUserFromFavorites(String username_)

- generateSearchIndex(Timestamp timestamp_)

- getFavoriteUsers(int startIndex_, int batchSize_, Integer sortProperty_, Integer sortOrder_)

- getFavoriteGroups(int startIndex_, int batchSize_, Integer sortProperty_, Integer sortOrder_)

### End-of-support for older versions of RDBMS

Version : 26.3

The following relational database management systems (RDBMS) either have already reached or are approaching the standard end-of-support dates set by their vendors and will no longer be supported in a future release of Appian. Customers are strongly advised to upgrade to a newer supported version .

### Anthropic Claude 3.5 Sonnet

Version: 26.2

Amazon Web Services (AWS) has scheduled the Anthropic Claude 3.5 Sonnet model for deprecation on March 1, 2026. This update will apply to all versions of Appian and impacts the following regions:

- US East (N. Virginia) us-east-1

- US West (Oregon) us-west-2

- Europe (Frankfurt) eu-central-1

- Europe (Zurich) eu-central-2

Review your current model usage now to ensure a seamless transition and maintain uninterrupted access to the most advanced AI capabilities in Appian. For more information about future model deprecations, see the model deprecation schedule .

### End-of-support for older versions of RDBMS

Version: 26.1

The following relational database management systems (RDBMS) either have already reached or are approaching the standard end-of-support dates set by their vendors and will no longer be supported in a future release of Appian. Customers are strongly advised to upgrade to a newer supported version .

## Feedback


---

## Appian 26.6 — synced 2026-08-16

Source: https://docs.appian.com/suite/help/26.6/Appian_Release_Notes.html

# Appian Release Notes

Share via

LinkedIn

Reddit

Email

Copy Link

Print

26.6 Product Webinar

Join our Appian marketing team and other Appian experts as they dig into highlights from the 26.6 release. You can also checkout our Release Showcase course on Academy Online to take a deeper dive into the latest features.

Join our Appian marketing team and other Appian experts as they dig into highlights from the 26.6 release. You can also checkout our Release Showcase course on Academy Online to take a deeper dive into the latest features.

Access new features and improvements every month on Appian Cloud

## Release Highlights

### Connect AI agents to external tools instantly with MCP

Version : 26.6

Expand the capabilities of your AI agents by connecting them directly to external enterprise systems using Model Context Protocol (MCP). Instead of building complex custom integrations for every third-party platform, you can now use a generic MCP connected system to link your AI agents to tools like GitHub, Snowflake, and Google Drive. This streamlined integration allows you to incorporate external capabilities into your AI agent's toolkit, eliminating development overhead and dramatically reducing your maintenance burden.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Use natural language to plan and build applications

Turn your requirements into working applications with Appian Composer and its new capability, dev agent —an intelligent assistant for end-to-end application development. This connected experience helps you organize development, delegate work to AI, and stay in control of every change.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

You can choose how much AI assistance to use as you build. Have Composer generate the foundational design objects for your application, or build manually and use the dev agent when you want AI support.

When you start building from Plan view, your stories become trackable development work on a kanban-style board , giving you a clear view of progress and the tasks that remain. When you're ready, simply assign specific tasks to the dev agent for automatic execution.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

Dev agent isn't limited to story tasks, either–—you can use plain language anytime to build brand-new design objects or edit existing ones on the fly. Instead of updating each record type, interface, process model, and expression rule individually, use specific and natural language to describe your overall goal for the business objects and application. Whether you're working from the Board tab , the Build view , or an interface object , the dev agent coordinates the necessary updates and accounts for dependencies between objects. Step-by-step previews and real-time feedback let you review each change, giving you the speed of AI-assisted development without losing oversight.

### Appian and Snowflake partner to activate data & AI in process

Version : 26.6

We've added native support for Snowflake—allowing you to put advanced data and AI intelligence to work within mission-critical business applications.

To get started, create a Snowflake connected system to access data from anywhere in Snowflake. From there, you can quickly build a record type that connects directly to your entire history of enterprise data in Snowflake. This unlocks instant access to your largest datasets alongside powerful features like relationships, record-level security, and custom record fields—all without syncing your data.

You can also equip your Appian AI agents with advanced Snowflake Cortex AI and ML capabilities through MCP. Snowflake Cortex AI enables custom model training for fraud and anomaly detection and much more, allowing you to more easily leverage industry-leading AI directly within Appian.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Introducing releases: A new way to manage deployments

Version : 26.6

Introducing " releases ," a new out-of-the-box way to manage and organize large deployments for your most interconnected apps. Releases allow you to group multiple packages of related functionality and easily deploy multiple packages from multiple apps at one time!

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

With releases, you can start organizing for deployment while you plan your team's development timeline. Once you've created your release, you can add it to your packages as you go! Then, when you're ready to deploy, breathe easy knowing all your team's work is already ready to go.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

Since releases have built in alerts to ensure that objects across releases don't overlap, using releases throughout development helps ensure your team is up-to-date with conflicting changes in your environment. These alerts help you avoid deploying features before they're ready by automatically highlighting when objects in packages are shared between multiple active releases.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

And, releases even help you stay organized after you deploy! Just deploy your packages, and we'll automatically group up the relevant objects into a new generated package for the release in your target environment. This helps you easily keep all your objects together in intermediate testing environments and make deploying to production environments a breeze.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

Releases are the ideal way to easily manage your development and deployment lifecycle. From sprint planning to deployment and beyond, releases provide you with native tooling for planning, tracking, and ultimately deploying your functionality, streamlining every step of your feature lifecycle.

### Deploy multiple packages from multiple apps in a single action

Version : 26.6

We're excited to announce that we're significantly streamlining deployments with the ability to deploy multiple packages from multiple app s in one deployment. Whether you're deploying manually, externally, or directly across environments, you can now select and deploy multiple packages from multiple apps in just a few clicks!

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

And, you'll notice that Compare and Deploy has a sleek new look and feel, perfect for moving quickly and efficiently through your deployment process.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

You can also start direct and manual deployments right from the Packages view, both for an individual app and the entire environment!

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

This new powerful approach to deployments not only speeds up the time to delivery, but also reduces effort, increases deployment flexibility and consistency, and helps you more confidently move from development to production.

## Deployments

### A new centralized view for packages

Version : 26.4

Experience a more unified way to work with the new Packages view in Appian Designer. Here, you can view and manage packages across your entire environment or within a single application.

Package view filters help you quickly find packages by name, application, releases, or even the objects within them. And, you can efficiently manage packages with bulk actions like associating multiple packages with a release or deploying multiple packages from the same app at once.

By unifying and simplifying package management in a single, intuitive view, we're helping you to stay organized and efficient from development to deployment.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### More comprehensive releases with package limit increase

Version : 26.5

You can now have up to 500 packages per app! By upping the limit from 100 to 500, your teams have more room to organize a full deployment cycle without running out of capacity. And, the higher limit means less frequent manual cleanup.

## AI Agents

### Accelerate AI agent prototyping with a unified build experience

Version : 26.6

Build, test, and refine your AI agents without ever losing your context. The enhanced Build tab for AI agents unifies configuration and testing into a sleek split-pane layout, saving you from switching tabs while you prototype. Keep your core instructions visible while managing tools, and reuse your saved test cases instantly from a new dropdown.

We've also made test results more readable by automatically formatting the text. Your tables, lists, and code blocks now show up beautifully in real time so you can review your work at a glance.

Speed up your design iterations and deploy production-ready AI agents faster than ever!

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Streamline AI agent evaluation

Version : 26.6

Deploy your AI agents with absolute confidence using a systematic quality workflow. The new Evaluate tab in the AI agent object provides a centralized space to manage your test cases and run them in bulk. Instantly verify performance across critical scenarios, catch regressions early, and review side-by-side results—no need to supervise individual runs.

We've also introduced inline feedback. Now, you can record clear thumbs-up or thumbs-down ratings directly on evaluation results. These insights automatically aggregate into powerful metrics like overall accuracy, right on the Evaluate tab.

With this centralized view of your test results, you'll immediately know when your AI agent is ready for production.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Accelerate AI automation with parallel tool execution

Version : 26.6

Accelerate your AI-driven business processes and cut operational costs with concurrent tool execution. Your AI agents now run multiple independent tool calls simultaneously instead of waiting through sequential, step-by-step workflows. This streamlined approach eliminates wait times and reduces AI action costs, getting your high-volume automations to the finish line faster.

### Engage users with chat agents

Version : 26.6

Create dynamic, conversational experiences for your users right inside your application layouts. With the new a!agentChatField component , you can confidently deploy dedicated Appian AI agents that communicate directly with your users through a chat interface. This makes it simple to embed real-time AI guidance directly into your daily workflows, transforming how your users interact with your applications.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

## Scale your enterprise AI strategy with the Appian MCP Server

Version : 26.6

Extend your enterprise AI strategy by linking Appian application data and workflows directly to third-party agent platforms. The new Appian Model Context Protocol (MCP) Server allows you to connect record types, process models, and expression rules as secure, discoverable tools for external agents. This centralized foundation ensures external assistants safely leverage Appian's robust security and underlying process logic without requiring custom connections or redevelopment.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

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

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

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

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

Further, use the optional Usage Groups input on the Execute Generative AI Skill smart service to map AI Action consumption directly to specific Appian groups, enabling precise cost attribution across departments.

The AI Skill test panel also displays AI Actions Consumed , so you can monitor consumption during development.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

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

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### A more connected Composer

Version : 26.6

Plan your applications with more continuity and speed using the updated chat in Composer . Your conversations now persist across every tab in the Plan view, eliminating the need to repeat context as you transition between tabs.

We've also polished the chat interface and formatting to make your interactions seamless and accessible. This streamlined experience provides an intuitive way to interact with your application plan and helps you keep your focus where it belongs—building great applications.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Upload rich files to ground your app in real requirements

Version : 26.6

Bring your existing assets directly into Composer to keep your plans grounded in your source material. You can now upload XML, YAML, and PPTX files , and up to 20 images, such as BPMN diagrams and screenshots of legacy UIs—all alongside your requirements. Every file you upload is automatically stored in Application Documentation, giving you built-in requirements traceability from day one.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

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

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Unlock the full power of your external documents

Version : 26.4

We're expanding the reach of your data fabric so you can integrate even more external documents into your applications. Now, you can use record types to access documents from connected system plug-ins , giving you the flexibility to unify your enterprise documents regardless of where they're stored.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

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

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Sync high-volume data with more flexibility

Version : 26.4

You can now leverage the Keep data available at high volumes setting with both incremental and smart service syncs . This added flexibility ensures your record types remain available at scale, regardless of how you choose to sync your data. If a sync ever exceeds your row limit, we'll automatically handle the overflow so your record types always have the latest information. It's never been easier to keep your most important data up to date and ready for action.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Analyze record view and action performance directly from your record types

Version : 26.4

We've made it easier to optimize your record views and actions by bringing query performance data directly into the record type's Performance page .

Now, you can instantly see how much data your record view or record action components are querying. This allows you to identify if those queries are slowing down your interfaces or requesting unnecessary fields—helping you build faster and more efficient interfaces and processes.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

## Integrations

### Connect your business processes to real-time Kafka events

Version : 26.6

Bring the power of event-driven architecture into your Appian applications with our Apache Kafka integration , the supporting event consumer object, and the Publish Event smart service.

Start by setting up your connection once with an Apache Kafka connected system . When the connected system is set up, create and configure a new event consumer object to link your Kafka topic to Appian.

With the event consumer , you can listen to a Kafka topic, filter incoming events using expressions, and automatically write records or trigger a process model for each matching event.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

With the Publish Event smart service , you can set up your process models to push vital data so other systems can take action on that information. To get started, add the new smart service, fill in the details of your Kafka broker, and specify the info you want to publish. Once the smart service is configured, Appian will start publishing events to the broker automatically.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

Whether you're processing new orders, flagging fraud, or onboarding employees, you can now connect your existing process models to activity happening across your enterprise—all without leaving Appian.

### Securely connect to Kafka brokers with OAuth and SCRAM

Version : 26.5

The Apache Kafka connected system now supports OAuth client credentials and Salted Challenge Response Authentication Mechanism (SCRAM) authentication for both SASL and SASL_SSL protocols. These capabilities ensure organizations can effortlessly meet rigorous Information Security (InfoSec) compliance standards without compromising ease of connectivity.

### Secure your PostgreSQL connections with OAuth 2.0

Version : 26.6

You can now use the OAuth 2.0 Client Credentials Grant to authenticate your PostgreSQL databases, whether you're using standard OAuth 2.0 or Azure AD. This new option provides another robust and effective layer of security for both synced and unsynced record types.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Granular scope control for HTTP connected systems

Version : 26.4

We're giving you more flexible OAuth 2.0 configurations for your HTTP connected systems . While most identity providers allow scopes in the request, those strictly following RFC 6749 require that the scope parameter is omitted during the backend token exchange. With one checkbox, you can now choose whether to include scopes during these token exchanges to meet different levels of OAuth spec compliance.

To ensure compatibility with your existing connected systems, this option is enabled by default. This keeps your integrations robust and reliable, no matter the requirements of your external data sources.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

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

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

And, to provide a unified development experience, we've added process reports as a supported report type in the report object . This allows you to configure report properties and deploy your process reports with your apps and packages.

With this update, we're giving you more power to uncover valuable, actionable insights into your business data.

### Discover suggested insights for count KPIs

Version : 26.5

Count KPIs measure critical process inefficiencies like stale cases, incidents, and other exceptions to your organization's typical workflow. With this release, we're helping you uncover the root cause of these issues more easily than ever with suggested insights.

Process HQ can now automatically generate suggested insights for your count KPIs, just like the existing insights for duration KPIs. Now, when you drill down to insights in your process, you can review the suggested insights, save them with a single click, and use them as a starting point for even deeper analysis.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Uncover suggested insights with the interactive process diagram

Version : 26.6

We're making it even easier to explore your process data and discover suggested insights , accelerating your time to real process improvements. Now, you can click on any activity or sequence in the process diagram to open more details and easily create a focused KPI with suggested insights. If the KPI is helpful, you can save it, or keep exploring the process diagram.

With this update, you can create KPIs and discover insights faster than ever before.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Easily discover and manage your datasets from Process HQ

Version : 26.4

Preparing your data for Process HQ is now more intuitive and efficient. The Data Governance page features a new semantic search, allowing you to find relevant record types without knowing the exact name.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

Once you've found your record type, you can review an AI-generated summary and choose whether to show the record type and its related record types as datasets . These enhancements give you the speed and control needed to quickly transform your information into actionable business insights.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Instantly view existing reports and dashboards for your datasets

Version : 26.4

The Data Catalog now gives you a more complete picture of how your organization uses its data. When you select a dataset, you'll instantly see all the reports and dashboards already built from it, as well as the specific data that makes up the dataset. This added visibility helps you avoid duplicating effort and ensures you have the context you need before you start building reports.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Set target performance for KPIs

Version : 26.4

We've added configurable targets for duration KPIs , so you can quickly see how well the KPI is performing compared to your expectations or goals. Use a target to easily measure the KPI's conformance to a standard value, or track progress towards a specific process improvement.

When you configure a target, we'll generate suggested insights to help you improve your processes and achieve your target performance.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Create and deploy business processes

Version : 26.4

We're continuing to improve the unified development experience for Process HQ with the new business process design object .

Now, instead of adding processes in production in Process HQ, developers can create business process objects during development in Appian Designer. This allows you to create Process HQ processes and deploy them just like any other design object, so processes are instantly available in Process HQ as soon as you deploy your app.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Design richer dashboards with adjustable layouts

Version : 26.5

Process HQ's easy-to-use dashboard builder just got even more powerful. You can now customize your dashboards exactly how you want! It's easy to adjust the height and width of reports and process KPIs when you drag and drop them onto a dashboard. And, you're even able to make items span multiple rows. Finer control over your dashboard layout is just a few clicks away.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Duplicate dashboards to build more quickly

Version : 26.6

We've added the ability to duplicate entire dashboards , so you can easily create new ones without having to start from scratch. The new dashboard will have all the same items and layout as the original, and you can even copy the security settings for easy sharing.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Visualize automation performance and opportunities in your process

Version : 26.5

This release, we're displaying more details about exactly who is performing each step of your process directly on the process diagram . Activity nodes now feature intuitive icons that show who or what is responsible for completing steps in your process—whether it's a human, RPA bot, AI agent, or integration—eliminating the need to cross-reference multiple sources. Simply hover over an icon to see a full breakdown of automation types for that activity.

This enhancement highlights critical insights into your hybrid workflows, helping you monitor AI performance and identify new automation opportunities with ease.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Expand your processes with more unique activities

Version : 26.5

We've expanded the limit for unique activities in a process from 50 to 100 to help you model the complex, high-density workflows that drive your enterprise.

### Customize your chart scale with axis settings

Version : 26.4

Report creators can now customize chart axes in reports to better highlight variance between data points, especially when comparing high-volume values. By adjusting the chart axis, you can make subtle trends and performance gaps visible at a glance.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Manage reports with the new action menu

Version : 26.4

We've added a new actions menu to reports pages, so common tasks are just a click away. Now you can view and edit report properties , duplicate a report , and add a report to an app , all without leaving the report page.

We've also updated the report properties to show the report's dataset, so users can easily identify the source of the report's data.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

## Appian Designer

### Build applications faster with a streamlined design object menu

Version : 26.4

We've tidied up the design object menu to help create a faster development experience. This streamlined menu lets you quickly browse all available design objects and stay focused on building your application.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

## Sites and portals

### Apply unique typefaces to individual sites and portals

Version : 26.5

Deliver a more tailored user experience by applying custom typefaces to specific sites and portals. Using CSS profiles , you can now independently select fonts for each site or portal, ensuring every page aligns with your specific brand guidelines. This granular control allows you to effortlessly manage diverse requirements across multiple brands or business units, all within a single Appian environment.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Expand your branding flexibility with new CSS profile properties

Version : 26.6

We're continuing to deliver more robust CSS profiles capabilities with the introduction of even more properties . In 26.4, we released properties to give you more control over the look of radio buttons, checkboxes, and card and box shadows, as well as to change the base font size across sites and portals.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

In 26.6, we're introducing properties that allow you to customize background colors for inputs and pop-up menus, such as those in text inputs and date pickers. Additionally, you can specify distinct colors for placeholder text, card borders, and box borders depending on whether the input appears on a light or dark background.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

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

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Take full control over your grid's search experience

Version : 26.6

You can now customize exactly how read-only grids search data. Use the new smartSearchType parameter to add lexical or semantic search to your grid on top of standard keyword search. Whether you're searching for exact terms or similar concepts, the smartSearchType parameter ensures you always find the most relevant results.

To further refine the experience and boost grid performance, the new searchFields parameter lets you specify exactly which fields to search. This parameter also allows you to search fields that aren't visible in the grid, like documents and extra long text fields, so your users can see a wider view of your data.

### Modernize grid designs with new styling and filter menus

Version : 26.5

We've made a series of enhancements to read-only and editable grids to provide a more intuitive and professional experience for your users.

In 26.4, we introduced new selection styling. Now, when some rows in a grid are selected, the checkbox in the grid header indicates that not all items are selected. We also improved the behavior of the search box and filters for read-only grids on ultra-wide screen monitors.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

Building on those updates, the 26.5 release offers even more flexibility for your grid's display. You can now choose the new LIGHT_WITH_OUTER_BORDERS style to show only row and outer borders for more design flexibility.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

Additionally, we added a new showManageFiltersMenu parameter to read-only grids so you can decide exactly when users can manage their own filters.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### More clarity for test scenarios

Version : 26.6

We've added an icon to interface test scenarios to show which scenario was last used, providing you with the context you need to efficiently test your interfaces.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Apply colors in the styled text editor

Version : 26.4

Enable users to enhance their content with new color and highlighting options in the styled text editor . Users can now apply text and highlight colors to their content, making it simple to create more impactful and scannable content.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### More color and size options for key components

Version : 26.6

You now have more options and flexibility when configuring key components. Tags , stamps , and rich text components now support the yellow "warn" color—making them more consistent with other components. And, you also can choose a smaller stamp size for even more flexibility when designing interfaces.

### More modern disabled input styling

Version : 26.6

We've refreshed the disabled state for input components to use opacity instead of a fixed color and also unified the style across all components. This change creates a clearer visual distinction between active and disabled fields, aligns with modern design standards, and allows more flexibility for the input background color CSS properties .

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

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

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

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

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Experience more reliable offline form interactions

Version : 26.6

We've enhanced the way your progress is saved and managed in offline forms to prevent data loss. When you submit, save a draft, or discard changes on an offline form, you will now see a loading indicator that confirms your request is being processed. This provides immediate visual feedback and helps prevent data errors, giving you peace of mind that your work is saved correctly every time.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

## Administration

### Identify and resolve frontend performance bottlenecks with Trace Explorer

Version : 26.5

Pinpoint performance bottlenecks in your interfaces, sites, and reports with Trace Explorer , a new self-service diagnostic tool for Appian Cloud environments. Available to administrators and developers in the environment-level Monitor view, Trace Explorer maps technical trace data to design objects—eliminating the need for manual log analysis or support cases. Use intuitive charts to visualize performance hotspots and analyze component-level response times to precisely optimize your front-end experiences. With direct access to actionable performance data, delivering a high-performance experience for your users is easier than ever.

### Customize your Forgot Password emails

Version : 26.6

You can now tailor Forgot Password emails to match your organization's brand, tone, and compliance requirements. Customization includes the option to create unique messages for each locale supported by your environment, giving each user cohort a more personalized experience.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

We've also built in placeholders to dynamically include vital information alongside your custom content. By customizing your site's emails in the Admin Console, you ensure that these messages align with your standards and speak clearly to your users.

### Monitor application performance with Dynatrace

Version : 26.4

Maximize the performance of your mission-critical applications with support for Dynatrace. If you use Dynatrace, a third-party observability platform, you can now enable it directly from the Admin Console to gain a unified view of your application health. This deeper visibility helps you identify and resolve bottlenecks faster, ensuring a consistently high-quality experience for your users.

### Stream your logs to Amazon S3

Version : 26.4

Monitoring your Appian Cloud environment is more flexible than ever. This release, we've expanded our log streaming capabilities to include support for Amazon S3 . With minimal setup in the Admin Console, you can easily stream logs directly to your own S3 buckets, giving you more control over how you retain and analyze data about your Appian environment.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

### Take control with self-service alerts

Version : 26.4

Note: This feature is available as a preview. Preview features are fully supported; however, they do not reflect the full functionality or performance of the feature yet.

We've introduced a new Self-Service Alerts dashboard in MyAppian that gives support contacts immediate visibility into issues affecting your Appian Cloud environment, such as long-running database transactions. A new banner in the Support page will also give a heads-up on any active alerts.

Plus, support contacts will receive email messages containing clear, actionable steps to resolve these issues at their own pace.

With these self-service tools, it's easier than ever to maintain a healthy environment for your organization.

Scroll or drag to pan · ⌘+/⌘− to zoom · Esc to close

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

## Feedback
