Morning Meeting 0905 10:30-11:05:

Duan:
1. bdcn's generalization on a single image can be improved. Consider adjusting parameters or model size without learning, or adjusting pidinet to suppress edge pixels.
2. The new classifier added to bdcn shows promise in suppressing unwanted parts, but needs more improvement. Ensure it works very well on the trained image. If the classifier is added at the final fusion layer, distance relationships may not be used. Consider adding the classifier at a shallower block. Evaluate this.

Han:
3. Fix one support for testing to compare results with Duan's.
4. Improve generalization (patch core) and suppress unwanted edges, especially in the AERO dataset.
5. Train dcama only on the metal dataset. Make necessary adjustments and send to Teams, priority higher than point 2.
6. Train dcama using only pidinet.
