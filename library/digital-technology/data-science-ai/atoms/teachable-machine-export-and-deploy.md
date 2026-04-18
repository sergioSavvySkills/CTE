---
atom_id: teachable-machine-export-and-deploy
title: Exporting and Deploying a Teachable Machine Model
subcluster: data-science-ai
credential_objectives:
  - certiport-its-artificial-intelligence::3.3
  - ms-ai-900::2.1
skill_type: skill
grade_band: HS
estimated_minutes: 45
difficulty: 3
prerequisites:
  - teachable-machine-introduction
status: draft
reviewer:
review_date:
---

## Learning objective

Students will be able to export a trained Teachable Machine model and embed it in a working web page or Python script that runs live predictions.

## Content stub

Skill lesson — students take the classifier they trained in the intro lesson and make it run outside Teachable Machine.

- **Export formats:** TensorFlow.js (runs in a browser), TFLite (runs on Android/Raspberry Pi), Keras (runs in Python); choose based on where you want the model to live
- **Embed in a web page:** Teachable Machine generates a snippet — paste into an HTML file; model runs in the visitor's browser with no server needed
- **Embed in Python:** download the keras model file; load with `tensorflow.keras.models.load_model()`; pass an image array to `model.predict()`
- **Test the deployed model:** run it on images it has never seen; compare to in-tool accuracy; identify drift between training environment and deployment environment

## Assessment stub

- Deploy: export your model as TensorFlow.js and get it running in a browser page that shows the predicted class label
- Test: find two images online that your deployed model gets wrong; write one sentence each explaining why
