1. What tool is used for annotation in dexined?
   Currently, I haven't found any; I recorded it in Word.
   
2. Is there any tool that uses canny for detection first, then annotation?
   There is a qt+canny tool, but drawing edges and deleting edges are too complicated. Manually drawn edges might be disconnected due to the pixels and big image size. Also, there's no undo button, requiring manual deletion and addition optimization. Canny's detection didn't achieve the desired edge effect. I recorded this in Word.
   Ultimately, we chose to use canny for initial detection results as a layer, then combine it with the original image in GIMP (GIMP's operations are quite convenient), and then optimize the edge details. Recorded this in Word.

3. When training flowers with dexined, continue related experiments such as:
   First, 70 epochs are too few; try increasing to see if it can fit. 
   Second, don't decrease the learning rate, keep training at 0.001.
   - Experiment 1: Learning rate at 0.001, step size [15, 20, 25, 30, 38,]; 70 epochs are too few; tried up to 300 epochs, still couldn't fit as well as pidinet.
   - Experiment 2: Learning rate 0.001, no step size setting, trained straight at 0.001: Effect started getting worse after 15 epochs, edges not detectable later. Perhaps because the learning rate remained high, causing weight drift and missing the minima.
   - Experiment 3: Learning rate 0.001, step size set at [15], learning rate reduced once in 15 epochs only: Effect worsened after 20 epochs. Same reasoning, high learning rate causes weight drift.
   - Experiment 4: Learning rate 0.001, step size set at [15, 20, 25], no reduction after 3 times. Effects similar to the first experiment. By the third reduction, the learning rate was too low, leaving little room for learning.

4. Trained an image on bdcn.
   Configured machine; started training on 7-person images; yet to test.

5. After annotating data, trained and tested an image.
   Training and testing show pidinet fitted well, proving my GT annotations are correct.
