# AFEC-X 2026 — Supervised Learning Hands-on

This activity introduces **supervised image classification** using butterfly photographs.

You may use **any one** of the following browser-based tools:

1. **Teachable Machine — Image Project**  
   https://teachablemachine.withgoogle.com/train/image

2. **SkillSafe Image Trainer**  
   https://image-trainer.skillsafe.ai/

3. **WebAI Playground — Image Classifier**  
   https://mlhs.ink/Playground/

Use whichever tool is accessible on your network.

The dataset and biological question are the same for all three tools.

---

# Learning goals

By the end of this activity, you should be able to explain:

- what a supervised-learning class label is;
- why training and test images should be separated;
- what a confidence score means;
- why a model can still make a confident prediction for an organism it has never seen;
- why model output is not automatically biological truth.

---

# The biological task

We will train a classifier using **four butterfly species**:

1. *Danaus chrysippus*
2. *Danaus genutia*
3. *Acraea terpsicore*
4. *Papilio polytes*

Then we will test the classifier using:

- held-out images from those same four species; and
- one species that was **never included in training**:

5. *Eurema hecabe*

---

# Dataset structure

The supervised dataset is stored in:

```text
data/supervised/
```

Training images:

```text
data/supervised/train/
├── Danaus_chrysippus/
├── Danaus_genutia/
├── Acraea_terpsicore/
└── Papilio_polytes/
```

Known-species test images:

```text
data/supervised/test/known/
├── Danaus_chrysippus/
├── Danaus_genutia/
├── Acraea_terpsicore/
└── Papilio_polytes/
```

Unknown-species challenge:

```text
data/supervised/test/unknown/
└── Eurema_hecabe/
```

## Very important

Do **not** use the images from:

```text
data/supervised/test/
```

during training.

The test images must remain unseen until after the model has been trained.

---

# Part A — Create the four classes

Regardless of which browser tool you use, create these four classes:

```text
Danaus chrysippus
Danaus genutia
Acraea terpsicore
Papilio polytes
```

Keep the species names exactly as shown so that everyone in the class is using the same labels.

---

# Part B — Add training images

For each class, upload the images from the matching training folder.

Example:

```text
Class: Danaus chrysippus

Upload from:
data/supervised/train/Danaus_chrysippus/
```

Repeat for all four species.

Before training, check that:

- all four classes are present;
- images are in the correct class;
- no known-test images were added;
- no *Eurema hecabe* images were added.

---

# Part C — Train the model

Train the classifier using the default settings first.

Do not spend time tuning model parameters during the first attempt.

The main goal is to understand the workflow:

```text
labelled examples
      ↓
training
      ↓
trained classifier
      ↓
prediction on unseen images
```

---

# Part D — Test with known species

Now use images from:

```text
data/supervised/test/known/
```

Test at least one image from each species.

For each test image, record:

| True species | Predicted class | Confidence | Correct? |
|---|---|---:|---|
| *Danaus chrysippus* |  |  |  |
| *Danaus genutia* |  |  |  |
| *Acraea terpsicore* |  |  |  |
| *Papilio polytes* |  |  |  |

## Questions

1. Did the model classify all four known species correctly?
2. Which image received the lowest confidence?
3. Did the highest confidence always correspond to the easiest image for you to identify?
4. What visual features might the model be using?

---

# Part E — Unknown-species challenge

Now open:

```text
data/supervised/test/unknown/Eurema_hecabe/
```

Choose one image.

Before testing it, remember:

> *Eurema hecabe* was never included in the training data.

Upload the image to the classifier.

Record the result:

| True species | Predicted class | Confidence |
|---|---|---:|
| *Eurema hecabe* |  |  |

Then test several more *Eurema hecabe* images.

---

# Pause and discuss

Ask yourself:

> Why did the model not say "I don't know"?

The classifier was only given four possible labels:

```text
Danaus chrysippus
Danaus genutia
Acraea terpsicore
Papilio polytes
```

It therefore tries to place the new image into one of the classes it knows.

Even when the correct biological class is absent, the model can still produce a prediction.

---

# Important concept — Closed-set classification

This activity demonstrates a **closed-set classifier**.

The model assumes that a new image belongs to one of the classes represented during training.

That assumption may be reasonable for some applications, but it can be dangerous in biodiversity monitoring because real field data may contain:

- species absent from the training set;
- damaged specimens;
- unusual life stages;
- novel species;
- non-target organisms;
- poor-quality images;
- environmental objects.

---

# Confidence is not biological certainty

Suppose the model predicts:

```text
Papilio polytes
Confidence: 82%
```

for an image of *Eurema hecabe*.

This does **not** mean:

> There is an 82% probability that the organism is truly *Papilio polytes*.

It means that, given the model and the classes available to it, *Papilio polytes* received the strongest model score.

The model was never given the correct answer as an option.

---

# Tool-specific instructions

## Option 1 — Teachable Machine

Open:

https://teachablemachine.withgoogle.com/train/image

Then:

1. Choose **Image Project**.
2. Choose **Standard Image Model**.
3. Create four classes.
4. Rename the classes using the four species names.
5. Upload the matching training images.
6. Click **Train Model**.
7. Use the preview/test area to test known-species images.
8. Finally test *Eurema hecabe*.

If Teachable Machine is unavailable on your network, use one of the alternatives below.

---

## Option 2 — SkillSafe Image Trainer

Open:

https://image-trainer.skillsafe.ai/

Then:

1. Create four image classes.
2. Name each class using the butterfly species names.
3. Add the matching training images to each class.
4. Train the classifier.
5. Test held-out known-species images.
6. Observe the confidence bars.
7. If available, inspect the held-out evaluation/confusion matrix.
8. Finally test *Eurema hecabe*.

This tool is particularly useful when you want a browser-based workflow without relying on Teachable Machine.

---

## Option 3 — WebAI Playground — Image Classifier

Open:

https://mlhs.ink/Playground/

Find **Image Classifier** and start the application.

Then:

1. Click **Add Class**.
2. Upload the first butterfly species dataset.
3. Add the remaining three classes.
4. Train the classifier.
5. Use **Predict** to test held-out known-species images.
6. Finally predict the *Eurema hecabe* images.

The interface may include additional model settings. For this workshop, use the default settings on the first run.

---

# Compare results with another group

If another group used a different browser tool, compare:

- predicted classes;
- confidence scores;
- which known images were misclassified;
- how *Eurema hecabe* was classified.

Do not expect the results to be identical.

Different tools may use different:

- pretrained models;
- image preprocessing;
- training procedures;
- random initialization;
- data splitting;
- confidence calculations.

The biological lesson should remain the same.

---

# Discussion questions

## 1. What did the model actually learn?

Did it learn butterfly taxonomy?

Or did it learn visual patterns associated with the labels we provided?

---

## 2. What happens when the world contains more classes than the model?

Our model knows four species.

A real biodiversity-monitoring camera may encounter hundreds or thousands.

What happens when an unrepresented species appears?

---

## 3. Would adding an "Unknown" class solve the problem?

It might help, but then ask:

> What images should be used to represent "unknown"?

The possible unknown biological world is extremely diverse.

---

## 4. What could make the classifier fail?

Possible examples:

- different lighting;
- different camera;
- different background;
- unusual wing position;
- damaged wings;
- sexual dimorphism;
- seasonal forms;
- small or blurry individuals;
- species not represented during training.

---

## 5. Is high accuracy enough?

A model can perform well on a familiar test set but still fail under new field conditions.

Evaluation should match the intended ecological use.

---

# Connection to the unsupervised activity

In this activity:

> **Humans defined the classes first.**

The model learned to distinguish the labels we supplied.

In the next activity, we will remove those labels and use K-means clustering.

Then the question changes from:

> "Which of my predefined classes does this image belong to?"

to:

> "What structure can the algorithm find in the data?"

---

# Take-home message

> **Supervised learning learns from the labels we provide.**

> **A model can only reason within the representation and classes it was trained on.**

> **Confidence is not the same as biological truth.**

> **AI predictions are evidence to evaluate, not biological truth to accept.**
