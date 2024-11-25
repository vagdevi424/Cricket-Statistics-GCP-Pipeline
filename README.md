# **End-to-End Data Pipeline for ICC ODI Batsmen Rankings**

This project implements an automated and scalable data pipeline to extract, transform, and visualize ICC ODI batsmen rankings. By leveraging **Google Cloud Platform (GCP)** services and orchestration tools, it showcases modern data engineering practices for processing and analyzing real-world data.

---

## **Overview**
The pipeline extracts cricket statistics from the **Cricbuzz API**, processes the data for quality and structure, and stores it in **BigQuery** for querying and analysis. The processed data is visualized in an interactive dashboard built with **Google Looker Studio**. Automation is achieved using **Apache Airflow** on **Cloud Composer**, which ensures seamless execution and monitoring of the pipeline.

---

## **Key Features**
1. **Data Extraction:**
   - Retrieves ICC ODI batsmen rankings in CSV format from the Cricbuzz API using a Python script.
   
2. **Data Transformation:**
   - Processes raw data using **Google Dataflow** with a custom JavaScript User-Defined Function (UDF).
   - Cleans and enriches the data, ensuring compatibility with the BigQuery schema.

3. **Data Storage:**
   - Stores raw data in **Google Cloud Storage (GCS)** and processed data in **BigQuery** for efficient querying and analysis.

4. **Orchestration:**
   - Uses **Apache Airflow** on **Cloud Composer** to automate task execution, including:
     - Data extraction
     - Upload to GCS
     - Triggering a Dataflow job
     - Validating the data in BigQuery.

5. **Data Visualization:**
   - Creates an interactive **Looker Studio dashboard** for analyzing batsmen rankings with features like country-based filtering and rank-specific insights.

   ![image](https://github.com/user-attachments/assets/de214e0b-af70-4093-a811-2f49c1efb53d)


---

## **Technologies Used**
### **1. Google Cloud Platform Services:**
   - **BigQuery**: Data warehouse for structured storage and analytics.
   - **Dataflow**: Distributed processing for data transformation and loading.
   - **Cloud Storage (GCS)**: Storage for raw data, metadata, and temporary files.
   - **Cloud Functions**: Serverless triggers for initiating Dataflow jobs.
   - **Cloud Composer**: Managed Airflow service for pipeline orchestration.

### **2. Programming Languages and Tools:**
   - **Python**: For data extraction scripts and orchestration.
   - **JavaScript UDF**: For data transformation in Dataflow.
   - **Google Looker Studio**: For interactive dashboards.
