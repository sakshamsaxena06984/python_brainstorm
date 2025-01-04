from joblib.numpy_pickle_utils import xrange

if __name__=='__main__':
    for ele in xrange(10):
        print(f"value: {ele} and type is : {type(ele)}")

    for ele in range(10):
        print(f"value: {ele} and type is : {type(ele)}")
