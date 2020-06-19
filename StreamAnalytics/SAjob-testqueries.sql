function createArray(pHLevel,temperature,soil_moisture,humidity,sunlight,hasWeed){
    var data={"pH":pHLevel,'Temperature':temperature,'Soil Moisture(%)':soil_moisture,'Humidity(%)':humidity,'Sunlight(lux)':sunlight,'HasWeed':hasWeed}
    return data
}


SELECT [EventEnqueuedUtcTime] as time ,udf.score(
udf.createArray([pH Level],[temperature(C)],[soil_moisture(%)],[humidity(%)],[sunlight(lux)],[HasWeed])
) 
INTO [Pottedviz]
FROM [Potted-data-stream]




WITH ml AS (
   SELECT [EventEnqueuedUtcTime] as time, udf.score(udf.createArray([pH Level],[temperature(C)],[soil_moisture(%)],[humidity(%)],[sunlight(lux)],[HasWeed])
) as result from [Potted-data-stream]
)
Select result
Into [Pottedviz]
From ml