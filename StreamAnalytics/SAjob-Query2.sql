SELECT [EventEnqueuedUtcTime] as time,[pH Level],
[temperature(C)],[soil_moisture(%)],[humidity(%)],[sunlight(lux)],[HasWeed]

INTO [Pottedviz]
FROM [Potted-data-stream]

