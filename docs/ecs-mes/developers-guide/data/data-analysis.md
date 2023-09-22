# Data Analysis

## Ignition Historical Analysis

The choice to use Ignition Tag History for data collections means that all the out-of-the-box functionality provided by the Ignition platform is available for accessing the raw data. There are many resources available that provide information and examples of how to extract, transform and visualize this data.  Below are some of the ways used by the ECS-MES application:

- To-do: list of resources describing how the raw data can be accessed

In the following sections, we will examine how the ECS-MES scripts/modules query this raw data and tranform into into the *MES Events* required for OEE and Downtime Analysis.

## MES Event Analysis

Events are state based and count based.

### MES State Event Analysis

Describe please.

### MES Count Event Analysis

Describe please.

## MES OEE Analysis

OEE stands for Overall Equipment Effectiveness, and it is a key performance metric used in manufacturing and production industries to measure and improve the efficiency and productivity of equipment and processes. OEE provides a holistic view of how well equipment is performing by considering three critical factors: Availability (A), Performance (P), and Quality (Q). These three components help organizations identify areas for improvement and optimize their manufacturing processes.

### Availability

Availability measures the percentage of time that a piece of equipment is available and ready for production when it is scheduled to be. It takes into account factors such as downtime due to equipment breakdowns, changeovers, maintenance, and other unplanned stoppages. The formula for Availability is typically calculated as:

```python
Availability = (Planned Production Time - Downtime) / Planned Production Time
```

Maximizing availability involves reducing unplanned downtime and ensuring that the equipment is ready to run when needed.

### Performance

Performance accounts for anything that causes the process to run slower than the max possible speed. It includes slow cycles and small stops.

To calculate performance, we look at the ratio between the number of units that were started and the number of units that should have been started.

First, we calculate how many units should have been started. Using the collected data, this is calculated as:

```txt
Standard Infeed Count = Standard Rate * Outfeed Scale * Runtime
```

Since the *Standard Rate* is specified in terms of the outfeed, we use the *Outfeed Scale* setting to convert express the standard rate in terms of the infeed.

Then, based on the *Counters* that are available, we calculate the number of units started (or Actual Infeed Count), using one of formulas from the following table:

| Infeed | Outfeed | Rejects | Formula |
| ------ | ------- | ------- | ----------------------------- |
| :heavy_check_mark: | :x: | :x: | `Infeed Count * Infeed Count Scale` |
| :x: | :heavy_check_mark: | :x: | `Outfeed Count * Outfeed Scale` |
| :x: | :heavy_check_mark: | :heavy_check_mark: | `(Outfeed Count * Outfeed Scale) + (Reject Count * Reject Count Scale)` |

A counter is considered *not available* if the value has not changed over the analysis time frame.

Finally, performance is calculated as follows:

```txt
Performance = Actual Infeed Count / Standard Infeed Count
```

### Quality

Quality evaluates the percentage of good, defect-free products or units produced by the equipment compared to the total number of products or units produced. It takes into consideration defects, rework, or scrap generated during the production process. The formula for Quality is usually calculated as:

```python
Quality = (Good Units Produced / Total Units Produced)
```

Enhancing quality involves reducing defects and ensuring that the products meet the required standards.
