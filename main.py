1. Dexined training from scratch. Documented.
   a. Learning rate 0.01, poor results.
   b. Learning rate 0.01, 0.001, poor results.
   c. Learning rate 0.01, 0.0001, poor results.
2. Testing BDCN with 7person from yesterday, then train with 1person.
   a. Tested 7person, fits well, worry about partial pixel read issue, check today.
   b. Training 1person started.
3. Labelme annotation tool.
   a. Useful, non-closed lines.
   b. Convert JSON to PNG, values are 0 and 255.
4. GIMP annotation tool.
   a. Dexined edge thickness ~5 pixels.
   b. Mr. Zhao recommended skeletonize method, useful, use it for industrial parts as they have many edges.
5. Continue annotating other datasets. Total 42 images.
   a. Airplane turbine blades: 6 remaining. Done.
   b. Circular cast objects: 16 remaining. Done.
   c. Third folder not a priority, annotated first object in the fourth folder, ball screws, 20 images. Done.
6. Training Pidinet with annotated three folders.
   a. Trained one image at a time, for-loop. Completed, pending test.

Today's plan:
1. Filter test images, delete non-compliant ones.
2. Test Pidinet model trained on one image for out-of-box performance on other test images.
3. Test BDCN for 1person performance.
4. Annotate second object in the fifth folder, Cylinder in 5-apple-company.
