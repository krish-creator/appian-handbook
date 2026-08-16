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
