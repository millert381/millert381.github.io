# Data Collection

Data collection is achieved by using [Ignition UDTs](https://docs.inductiveautomation.com/display/DOC81/User+Defined+Types+-+UDTs). Each [Equipment](blank) definition in the [Equipment Model](blank) corresponds to a [UDT Instance](blank). Each UDT instance should inherit from the [Base UDT](blank), which is responsible for historizing equipment data via [Ignition's Tag Historian](https://docs.inductiveautomation.com/display/DOC81/Tag+Historian+Module).

The following table shows all the data points collected (in real-time) that are later used for OEE and Downtime Analysis.

| Data Point | Data Type | Description |
| ---------- | --------- | ----------- |
| Counters/Infeed | long | Infeed Counter |
| Counters/Outfeed | long | Infeed Counter |
| Counters/Reject | long | Infeed Counter |
| Mode | int | The overall status of the equipment (ex. Production, Changeover, CIP, etc.); maps to an [Equipment Mode]() defined in the [Equipment Mode Class]() that is assigned to this Equipment. |
| Note | int | The note field allows a user to provide additional context during a downtime event. |
| Product | int | Equipment mode |
| Production Settings/Infeed Scale | float | A value used to scale the infeed count to the actual number of units. |
| Production Settings/Infeed Units | str | The units for the infeed count (ex. bags, bottles, cans, cases, pallets, pouches, etc.) |
| Production Settings/Outfeed Scale | float | A value used to scale the outfeed count to the actual number of units. |
| Production Settings/Outfeed Units | str | The units for the outfeed count (ex. bags, bottles, cans, cases, pallets, pouches, etc.) |
| Production Settings/Rate Period | str | Period of time associated with the *Schedule* and *Standard* Rate. Used for display purposes; hard-coded to **minutes**. |
| Production Settings/Reject Scale | float | A value used to scale the rejects count to the actual number of units. |
| Production Settings/Reject Units | str | The units for the reject count (ex. bags, bottles, cans, cases, pallets, pouches, etc.) |
| Production Settings/Schedule Rate | float | The rate at which the equipment is realistically expected to run. (in **minutes**) |
| Production Settings/Standard Rate | float | The ideal rate at which the equipment could run for the given product.  Note: This is not necessarily the nameplate design speed; it is common this value will vary depending on the type of product being run. |
| Shift | str | The shift assigned to the equipment via the [ECS MES Scheduler](blank) |
| State | int | The specific status of the equipment (ex. Running, Starved, Blocked, etc.); maps to an [Equipment State]() defined in the [Equipment State Class]() that is assigned to this Equipment. |
| Work Order | str | A work order identifier, commonly used to tie back to ERP systems. |

## Infeed, Outfeed, Reject, and Auxiliary Counts

By default, the three main counters available for data collection are: Infeed, Outfeed, Reject.

Additional counters can be added if desired for future analysis; however, these three counters are the only ones considered when performing OEE Analysis. The table below describes how these counters are used 

## Collect State Changes (Running, Downtime, Starved, Blocked, Idle)

### Collect Downtime Reason Codes for Downtime Events


### PLCs should be reporting WHY you are in the Downtime state.



## Collect Mode Changes (Production, Planned Downtime, Maintenance, CIP, etc)
### May have scenarios where an overall line status overrides the statuses of the individual cells. For example, a Filler in "CIP Mode" might cause all cells to enter "CIP Mode" as well.
## Collect Shift (Use IA Shift Config or custom built shift configuration?)
### Ignition's Shift cannot be overridden for one time (you have to remember to "fix" the schedules after your override situation).
### Swedish Match uses a tag collector that looks up the shifts from a database where the shifts are configured in advance by supervisors/schedulers.
### Possibly implement a hybrid that stores exceptions to the Ign configured schedule only.
## Historize production settings (similar to tag collectors)
### UDT tag members w/ historian configuration.

