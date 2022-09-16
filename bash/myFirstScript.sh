DATA=$(curl https://api.covidtracking.com/v1/us/current.json)
POSITIVE=$(echo $DATA | jq '.[0].positive')
NEGATIVE=$(echo $DATA | jq '.[0].negative')
PENDING=$(echo $DATA | jq '.[0].pending')
DEATHS=$(echo $DATA | jq '.[0].death')
STATES=$(echo $DATA | jq '.[0].states')
HOSPITALIZED=$(echo $DATA | jq '.[0].hospitalized')
TODAY=$(date)

echo "On $TODAY, there are currently $STATES states affected by COIVD, there were $POSITIVE positive COVID cases, there were $NEGATIVE negative cases, there are currently $PENDING pending cases, there are currently $HOSPITALIZED hospitalized from COVID, and there are $DEATHS deaths from COVID."  


