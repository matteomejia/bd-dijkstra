#!/bin/bash

run() {
    hadoop jar $HADOOP_HOME/hadoop-streaming.jar -input input/$inputfile -output output -mapper mapper.py -reducer reducer.py -file mapper.py -file reducer.py
    hdfs dfs -cat output/* > result.txt
    hdfs dfs -rm -r output
    hdfs dfs -rm input/*
    hdfs dfs -copyFromLocal $inputfile input/$inputfile
    inputfile="result$i.txt"
    echo "iter $i"
}

main() {
    for ((i = 1; i <= $iterations; i++));
    do
        run $i
    done
}

inputfile=$1
iterations=$2