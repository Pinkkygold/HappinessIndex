# test_model.py
import joblib
import numpy as np

try:
    # Try to load the model
    model = joblib.load('BostonHouses_model.pkl')
    print("✅ Model loaded successfully!")
    print(f"Model type: {type(model)}")
    
    # Test with sample data
    sample_data = np.array([[0.00632, 18.0, 2.31, 0, 0.538, 6.575, 65.2, 4.0900, 1.0, 296.0, 15.3, 396.90, 4.98]])
    
    print(f"Sample data shape: {sample_data.shape}")
    
    # Try to predict
    prediction = model.predict(sample_data)
    print(f"Prediction: {prediction}")
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()