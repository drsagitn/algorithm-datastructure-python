export const themes = [
  {
    id: 1,
    title: "Teamwork and Collaboration",
    questions: [
      {
        question:
          "On a team project. What role did you play, and how did you contribute to its success?",
        answer: `**Situation:** Our team was tasked with developing a real-time fraud detection system to analyze transaction patterns.
  **Task:** As the Senior AI Engineer, my responsibility was designing the data pipeline and integrating the machine learning model.
  
  **Action:** 
  - Collaborated with data scientists to fine-tune the model.
  - Worked with backend engineers to ensure the system could handle high transaction volumes.
  - Led the deployment process.
  
  **Result:** The system reduced fraud levels by over **95%**, saving the company millions within months of deployment.`,
      },
      {
        question:
          "Difficult team member. How did you handle it?",
        answer: `**Situation:** A teammate consistently missed deadlines, which delayed our sprint goals.
  
  **Task:** I needed to address this issue without creating conflict.
  
  **Action:** 
  - Scheduled a one-on-one to understand their challenges and discovered they were struggling with new tools.
  - Provided additional training and paired them with a more experienced team member.
  
  **Result:** Their performance improved, and our team met all subsequent sprint deadlines.`,
      },
      {
        question:
          "Handle disagreements within a team? Can you provide an example?",
        answer: `**Situation:** During the design of an anomaly detection system, there was a disagreement over whether to use a batch processing or streaming architecture.
  
  **Task:** My role was to mediate and ensure the best choice for the project.
  
  **Action:** 
  - Facilitated a discussion and gathered performance metrics from both approaches.
  - Demonstrated the advantages of a streaming solution for our real-time needs.
  
  **Result:** The team adopted the streaming architecture, enabling faster detection and response times.
  
  ---
  
  **Alternative Situation:** During the development of our fraud detection system, there was a disagreement between me and a teammate over whether to implement additional rules alongside the machine learning model. They believed the model alone was sufficient, while I advocated for a hybrid approach to improve resilience against fraudsters.
  
  **Task:** Resolve the disagreement constructively and ensure the project benefited while maintaining a positive team dynamic.
  
  **Action:** 
  - Initiated a discussion to understand their perspective and shared mine with data-driven insights.
  - Suggested creating a proof of concept to test both approaches.
  - Facilitated the experiment using real transaction data to compare effectiveness.
  
  **Result:** The hybrid solution reduced fraud rates by an additional **15%** without impacting system performance. The team acknowledged the value of the combined approach, and we implemented it more broadly. This experience strengthened our collaboration and highlighted the importance of data-backed decision-making.`,
      },
      {
        question: "Helped a teammate improve their performance.",
        answer: `**Situation:** A junior developer was struggling to understand distributed data processing frameworks.
  
  **Task:** Help them contribute effectively to a large-scale data pipeline project.
  
  **Action:** 
  - Mentored them through hands-on sessions.
  - Explained the principles of distributed computing.
  - Provided sample projects for practice.
  
  **Result:** They became proficient in **Spark** and **Kafka**, eventually taking ownership of key components of the pipeline.`,
      },
      {
        question:
          "Made a mistake that affected a colleague. How did you rectify things?",
        answer: `**Situation:** While building a data pipeline for a fraud detection system, I misconfigured a Kafka topic partition, which caused delays in the data processing pipeline. As a result, the machine learning model trained by a data scientist was receiving incomplete data.
  
  **Task:** Quickly identify and fix the issue while minimizing further disruptions for the data scientist. Ensure this kind of error wouldn’t happen again.
  
  **Action:** 
  - Took ownership of the mistake and informed the data scientist.
  - Reviewed the configuration, identified the misstep, and corrected the partitioning logic.
  - Added automated monitoring to alert the team of irregularities in data ingestion.
  - Created detailed documentation for handling Kafka configurations.
  
  **Result:** The pipeline was restored within hours, allowing the data scientist to continue without major delays. I received appreciation for taking responsibility and proactively resolving the problem. The monitoring system also improved overall team efficiency.`,
      },
    ],
  },
  {
    id: 2,
    title: "Leadership and Influence",
    questions: [
      {
        question:
          "Took the lead on a project. What was the outcome?",
        answer: `**Situation:** I led a project to build a data processing pipeline for defect detection.
  **Task:** My goal was to ensure seamless ingestion, processing, and scoring of high-volume data.
  
  **Action:** 
  - Designed the architecture.
  - Established clear milestones.
  - Led a cross-functional team of engineers and data scientists.
  
  **Result:** The pipeline went live as scheduled and significantly reduced the cost and execution time.`,
      },
      {
        question:
          "Influenced someone to adopt your idea.",
        answer: `**Situation:** A team preferred a batch processing model for fraud detection, but I proposed a real-time solution.
  
  **Task:** Convince them of the benefits of real-time processing.
  
  **Action:** 
  - Presented a proof of concept showing how real-time scoring reduced fraud latency.
  - Supported the proposal with performance benchmarks.
  
  **Result:** The team adopted real-time processing, leading to faster fraud prevention.`,
      },
      {
        question:
          "Mentored someone? How did you approach it, and what was the result?",
        answer: `**Situation:** I mentored a junior developer working on a data ingestion system.
  
  **Task:** Help them understand best practices for scalable and efficient pipeline development.
  
  **Action:** 
  - Paired with them on key tasks.
  - Provided feedback during code reviews.
  - Encouraged them to present their work during team meetings.
  
  **Result:** They successfully delivered their component and gained confidence in their abilities.`,
      },
    ],
  },
  {
    id: 3,
    title: "Adaptability and Learning",
    questions: [
      {
        question:
          "Learn something new quickly to complete a project?",
        answer: `**Situation:** I had to learn PyTorch to build an anomaly detection model.
**Task:** Deliver the model within a tight deadline.
**Action:** 
- Took online courses.
- Read documentation.
- Applied the knowledge directly to the project.
**Result:** The model was delivered on time and performed with high accuracy.`,
      },
      {
        question: "Adapt to a significant change.",
        answer: `**Situation:** A last-minute shift required migrating from CosmosDB to SQL for saving costs.
**Task:** Ensure the migration was seamless.
**Action:** 
- Quickly researched and developed data migration tools.
- Reconfigured the system architecture.
**Result:** The migration was completed successfully with minimal downtime.`,
      },
      {
        question:
          "Were right about something but had to do or say something differently than you otherwise would’ve.",
        answer: `**Situation:** While working on the real-time fraud detection system, I identified a technical approach that I was confident would significantly improve model accuracy. However, I was aware that the approach was highly unconventional and might initially be met with resistance from my colleagues.

**Task:** Ensure that the solution would be embraced by the team without alienating anyone.

**Action:** 
- Framed the idea as a collaborative exploration.
- Initiated discussions to understand the team's concerns and thoughts on the current approach.
- Proposed a small-scale proof of concept to compare results objectively without disrupting ongoing efforts.
- Presented the data-driven reasoning behind my proposal.

**Result:** The proof of concept demonstrated that my approach improved fraud detection rates with minimal additional processing time. The team acknowledged its effectiveness, and we implemented it more broadly. This approach built trust within the team and strengthened collaboration.`,
      },
      {
        question:
          "Deadline has been moved up—how do you handle it?",
        answer: `**Situation:** While deploying a real-time fraud detection system, the client unexpectedly moved the go-live date up by two weeks to coincide with a major product launch.

**Task:** Reprioritize work, address potential risks, and deliver a high-quality solution within the revised timeline.

**Action:** 
- Gathered the team to reassess priorities and create a streamlined plan.
- Identified critical tasks, such as model deployment, pipeline scalability, and alerting mechanisms.
- Deferred non-essential features, like advanced reporting, to a post-launch phase.
- Increased communication with stakeholders to set clear expectations.
- Introduced daily stand-ups to monitor progress and address roadblocks quickly.
- Conducted focused testing to ensure the core functionality met quality standards.

**Result:** The system was successfully deployed on the accelerated timeline and performed reliably during the client’s launch event. The client was impressed with the system’s performance and our collaborative approach. This experience reinforced my ability to adapt under pressure and deliver results without compromising quality.`,
      },
    ],
  },
  {
    id: 4,
    title: "Problem-Solving and Challenges",
    questions: [
      {
        question: "A challenging problem you faced and how you solved it.",
        answer: `**Situation:** When we first deployed our machine learning model for fraud detection, fraudsters quickly adapted by trying different transaction patterns to bypass the system. This increased the model's workload and risked exposing its vulnerabilities.

**Task:** Protect the model from being overwhelmed while ensuring fraud detection remained effective.

**Action:** 
- Introduced a secondary rule-based system to handle retry attempts.
- Designed the rules to quickly block repeated fraud attempts while preserving the model’s capacity for genuine cases.

**Result:** This strategy significantly reduced the model's workload and effectively stopped fraudsters from probing the system. It maintained the model’s integrity and accuracy, leading to sustained fraud prevention success.`,
      },
      {
        question: "A time when you failed. What did you learn, and how did you move forward?",
        answer: `**Situation:** During an anti-fraud project, I underestimated the complexity of integrating third-party APIs, causing delays.

**Task:** Address the delay and regain stakeholder trust.

**Action:** 
- Analyzed the bottlenecks.
- Re-prioritized tasks.
- Brought in an external consultant to speed up the integration process.

**Result:** The project was completed successfully, and I learned the importance of thorough dependency assessment during planning.`,
      },
      {
        question: "Prioritize tasks when faced with multiple high-priority deadlines?",
        answer: `**Situation:** I had overlapping deadlines for building a fraud model and addressing a critical production bug.

**Task:** Ensure both were resolved promptly.

**Action:** 
- Prioritized the production bug for immediate resolution.
- Delegated parts of the model development to teammates.
- Provided oversight for both tasks to ensure progress.

**Result:** The production issue was resolved within hours, and the model development stayed on track.`,
      },
      {
        question: "Solved a problem with an innovative solution.",
        answer: `**Situation:** A manual process for providing feedback on flagged transactions was causing delays and high operational costs.

**Task:** Automate and streamline the process.

**Action:** 
- Designed a feedback loop system that integrated ML predictions and rule-based thresholds into a daily tool like Slack for quick approvals.

**Result:** Review time dropped from hours to minutes, reducing costs by **30%**.`,
      },
    ],
  },
  {
    id: 5,
    title: "Customer Obsession and Impact",
    questions: [
      {
        question: "Worked on problem significant impact on the customer or business.",
        answer: `**Situation:** I developed a fraud detection pipeline for real-time transaction scoring.

**Task:** Ensure fraud levels dropped without impacting legitimate transactions.

**Action:** 
- Implemented a scalable architecture.
- Integrated continuous model retraining to adapt to evolving fraud patterns.

**Result:** Fraud rates dropped to near-zero, saving millions for the business.`,
      },
      {
        question: "Building Trust Through Transparency",
        answer: `**Situation:** After deploying a new fraud detection model, some customers expressed concerns about false positives, as legitimate transactions were occasionally blocked.

**Task:** Address customer concerns while maintaining the system's effectiveness.

**Action:** 
- Introduced a feature that explained why a transaction was flagged, providing transparency to customer support teams.
- Worked with the customer success team to gather feedback and fine-tune the model to reduce false positives.

**Result:** The changes led to a **30% decrease in false positives** and significantly improved customer trust, as reflected in higher Net Promoter Scores (NPS).`,
      },
      {
        question: "Quick Response to Critical Issues",
        answer: `**Situation:** A key customer reported a major issue with our fraud detection system, where legitimate transactions were incorrectly flagged during a holiday sales peak. This risked damaging their reputation and revenue.

**Task:** Resolve the issue quickly and reassure the customer.

**Action:** 
- Identified that a recent model update caused the problem and immediately rolled back to a stable version.
- Worked overnight with the team to debug the issue, refine the model, and deploy a patch.
- Maintained communication with the customer throughout the process to keep them informed.

**Result:** The issue was resolved within **24 hours**, and the customer’s operations returned to normal with no long-term impact on their business. Their feedback highlighted our responsiveness as a key reason for continuing the partnership.`,
      },
      {
        question: "Help a client figure out what they want when they’re not sure?",
        answer: `**Situation:** While working on a fraud detection system for a retail client, they wanted "better fraud prevention" but were unsure about specific features or metrics to define success.

**Task:** Help the client clarify their needs, define measurable goals, and translate those into technical requirements for the solution.

**Action:** 
- Asked targeted questions about their challenges, such as:
  - What types of fraud were causing the biggest issues?
  - How were fraudulent activities currently being detected and mitigated?
  - What metrics or KPIs would indicate success (e.g., fraud losses, false positives)?
- Conducted a workshop with their operations team to identify pain points and opportunities for improvement.
- Created prototypes demonstrating solutions for real-time alerts, transaction scoring, and user-friendly dashboards.

**Result:** The client clarified their priorities, focusing on reducing false positives and creating actionable insights. We tailored the solution to include a hybrid model with explainability features. Deployment reduced fraud losses by **60% within three months** and significantly improved operational efficiency.`,
      },
    ],
  },
  {
    id: 6,
    title: "Inclusion and Diversity",
    questions: [
      {
        question: "Worked with a diverse team. How did you ensure everyone felt included?",
        answer: `**Situation:** My team included members from different cultural backgrounds and expertise levels.

**Task:** Foster an inclusive environment.

**Action:** 
- Encouraged everyone to share their perspectives.
- Celebrated diverse ideas and contributions.
- Adjusted workflows to ensure inclusivity for all team members.

**Result:** The team’s collaboration improved significantly, leading to a successful project outcome.`,
      },
      {
        question: "How have you advocated for inclusivity in a project or team?",
        answer: `**Situation:** A junior team member was hesitant to share their ideas during meetings.

**Task:** Ensure they felt comfortable and empowered to contribute.

**Action:** 
- Provided encouragement during meetings.
- Actively asked clarifying questions to validate their input.
- Created a safe space for open dialogue and sharing ideas.

**Result:** They became an active contributor, and their ideas directly improved project outcomes.`,
      },
    ],
  },
  {
    id: 7,
    title: "How You Work with Yourself & Manage Your Time",
    questions: [
      {
        question: "How do you manage your time effectively?",
        answer: `**Situation:** While leading the development of an anomaly detection model for fraudulent transactions, I had to manage the dual responsibilities of delivering the model on a tight deadline while supporting ongoing production systems and mentoring junior developers.

**Task:** Meet the project timeline without compromising the quality of day-to-day operations or neglecting leadership responsibilities.

**Action:** 
- Broke the project into smaller milestones and prioritized tasks based on impact and urgency.
  - High-priority tasks, such as deploying real-time fixes for production issues, were handled immediately.
  - Project-specific tasks, like model tuning and feature engineering, were scheduled in focused blocks of time to minimize distractions.
  - Delegated less critical operational tasks to team members, providing them with support and guidance.
- Used tools like Jira for task tracking and conducted daily stand-ups to align the team and address blockers quickly.
- Communicated regularly with stakeholders to manage expectations effectively.

**Result:** The model was delivered on time, and day-to-day operations ran smoothly. Delegation efforts empowered team members, with one junior developer taking ownership of a key pipeline component, enhancing their confidence and skills.`,
      },
      {
        question: "Worked effectively under pressure.",
        answer: `**Situation:** During a holiday shopping season, our fraud detection system experienced an unexpected spike in flagged transactions, leading to delays for legitimate customers and mounting frustration from a key retail client. The issue threatened to disrupt their peak sales period and required immediate resolution.

**Task:** Quickly identify the root cause, implement a fix, and restore confidence in our system while minimizing customer impact.

**Action:** 
- Assembled a small task force to diagnose the problem and worked through the night analyzing transaction logs.
- Identified that a recent rule update was overly restrictive for certain legitimate transaction patterns.
- Reverted the rule change as a temporary fix and proposed a dynamic threshold solution to adjust the model’s thresholds based on transaction context.
- Provided hourly updates to the client on progress and timelines for a permanent fix.

**Result:** Within **12 hours**, the system was stabilized, and the backlog of flagged transactions was cleared. The dynamic threshold solution was implemented shortly after, reducing false positives by **30%** during high-traffic periods. The client praised our responsiveness and continued their partnership for future seasons.`,
      },
    ],
  },
  {
    id: 8,
    title: "Microsoft-Specific Focus",
    questions: [
      {
        question: "Demonstrated one of Microsoft's leadership principles, such as 'Empower others' or 'Act with integrity.'",
        answer: `**Situation:** A junior engineer was struggling with a task.
  
  **Task:** Help them succeed without undermining their confidence.
  
  **Action:** 
  - Guided them through the task by asking questions to help them discover solutions independently.
  - Provided support and reassurance without directly solving the problem for them.
  
  **Result:** They completed the task successfully and gained confidence for future challenges.`,
      },
      {
        question: "Why do you want to work at Microsoft, and how do your values align with Microsoft’s mission?",
        answer: `I admire Microsoft’s mission to empower every person and organization on the planet to achieve more. This aligns with my passion for building impactful technology that improves lives. I’m excited to contribute to innovative projects, particularly in areas like AI and people understanding.`,
      },
      {
        question: "Why are you looking to leave your current employer?",
        answer: `I've had a great experience in my current role, and I'm proud of the impactful work I've contributed, such as developing an anti-fraud system that reduced fraud levels significantly in real-time. However, I'm looking for new challenges and opportunities to grow.
  
  At Microsoft, I see the chance to work with systems at global scale and collaborate with world-class teams to drive innovation using cutting-edge technologies. This role aligns with my goals of expanding my technical expertise and collaborating with other top talents to create meaningful impact. This is the next step forward in my career path.`,
      },
      {
        question: "What has motivated you to apply for a role with Microsoft?",
        answer: `Microsoft stands out to me because of its strong focus on creating impactful products at scale. I'm impressed with how the company integrates AI and data-driven solutions to improve collaboration and productivity, for example, Microsoft 365 and Copilot—areas I'm passionate about.
  
  From a professional perspective, I value Microsoft's emphasis on engineering excellence and growth mindset. The opportunity to work in an environment where I can contribute to cutting-edge systems used by millions while also learning from world-class engineers is incredibly motivating.
  
  The role I applied for aligns closely with the type of work I'm passionate about and experienced in. I've spent much of my career building scalable systems and analyzing collaboration patterns, and an opportunity to apply those skills to Microsoft products is very exciting.`,
      },
      {
        question: "Can you give me a brief summary of your experience and the technologies you have worked on?",
        answer: `Sure, my name is Thinh. I've been working as a full-stack engineer for 14 years, gaining experience in designing and implementing scalable, high-impact systems across frontend, backend, and data-driven AI solutions.
  
  **Technologies:** 
  - Languages: Python, C#, JavaScript, TypeScript, Java, PHP, C++.
  - Frameworks: .NET, Spring, React.
  - Infrastructure: Kubernetes, Redis, Spark, Databricks.
  - Databases: MSSQL, Postgres, MongoDB.
  - Cloud Platforms: Azure Cloud, Google Cloud, AWS.
  
  Currently, I'm a Senior AI Engineer at Vipps, focusing on leveraging AI and data pipelines to address complex challenges. One of my recent projects was an anti-fraud system where I developed a data pipeline to analyze criminal behaviors during fraud attempts. This system enabled real-time transaction scoring and delivered remarkable results—reducing fraud levels from monthly millions (NOK) to almost zero within months.
  
  I've also had the opportunity to work in different countries (Vietnam, South Korea, and now Norway), experiencing diverse working cultures. What I enjoy most about software engineering is solving challenging problems and delivering solutions that create tangible impacts, whether enhancing user experiences or improving security. I'm driven to learn and grow, adopting new technologies and collaborating with cross-functional teams to achieve meaningful outcomes.`,
      },
    ],
  },
  {
    id: 9,
    title: "Your Professional Ethics & Goals",
    questions: [
      {
        question: "A time you felt as though you weren’t doing your best work?",
        answer: `**Situation:** Early in my role as a Senior AI Engineer, I was assigned to build a proof of concept for a fraud detection model on a tight deadline. Eager to deliver quickly, I focused heavily on the technical aspects, such as building and fine-tuning the model, without spending enough time gathering input from stakeholders or fully understanding the real-world challenges they faced.
  
  **Task:** Deliver a model that could effectively detect fraudulent transactions. However, the lack of stakeholder alignment resulted in a solution that didn’t fully address their needs.
  
  **Action:** 
  - During a review meeting, I realized the model’s outputs were difficult for the client’s operations team to interpret, limiting its usability.
  - Paused further development to engage directly with stakeholders and better understand their workflows and expectations.
  - Collaborated with the client-facing team to design user-friendly outputs, including explainable risk scores and actionable insights.
  
  **Result:** Although the project took slightly longer, the final solution was much more aligned with the client’s needs. It was well-received and had a significant impact on reducing fraud while being easy for the team to use. This experience taught me the importance of balancing technical execution with stakeholder engagement, a lesson I’ve applied to every project since.`,
      },
    ],
  }
  
  
];
