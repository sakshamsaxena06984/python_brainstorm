
def frequencySort(s: str) -> str:
        freq = {}

        for c in s:
            freq[c] = 1 + freq.get(c, 0)
        print(freq)

        freq = sorted(freq.items(), key=lambda x: -x[1])

        return ''.join([key * val for key, val in freq])

def minimumMove(arr: []) -> int:
    print(arr)
    arr.sort()
    print(arr)
    m=arr[len(arr)//2]
    ans=0
    for ele in arr:
        ans=ans+abs(m-ele)
    return ans

'''
Project name
qwiklabs-gcp-00-b2c4c646f65c
Project number
825486355785
Project ID
qwiklabs-gcp-00-b2c4c646f65c
qwiklabs-gcp-00-b2c4c646f65c
qwiklabs-gcp-00-b2c4c646f65c

qwiklabs-gcp-00-b2c4c646f65c

qwiklabs-gcp-00-b2c4c646f65c

cd $BASE_DIR
mvn compile exec:java \
-Dexec.mainClass=../training-data-analyst/quests/dataflow \
-Dexec.cleanupDaemonThreads=false \
-Dexec.args=" \
--project=${PROJECT_ID} \
--region=${REGION} \
--stagingLocation=${PIPELINE_FOLDER}/staging \
--tempLocation=${PIPELINE_FOLDER}/temp \
--runner=${RUNNER}"
------------

cd $BASE_DIR
mvn compile exec:java \
-Dexec.mainClass=${MAIN_CLASS_NAME} \
-Dexec.cleanupDaemonThreads=false \
-Dexec.args=" \
--project=${PROJECT_ID} \
--region=${REGION} \
--stagingLocation=${PIPELINE_FOLDER}/staging \
--tempLocation=${PIPELINE_FOLDER}/temp \
--runner=${RUNNER}"

121@airtel.com
'''

if __name__=='__main__':
    s="tree"
    # print(frequencySort(s))
    print(minimumMove([1,3,2]))
