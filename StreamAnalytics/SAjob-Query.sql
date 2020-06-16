SELECT
    [temperature(C)],[humidity(%)],[pH Level],[sunlight(lux)],[soil_moisture(%)],[EventEnqueuedUtcTime] as time
INTO
    [Pottedviz]
FROM
    [Potted-data-stream]