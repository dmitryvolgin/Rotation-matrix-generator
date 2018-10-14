# Rotation-matrix-generator
Makes rotation matrix out of *Euler angles*.  
[Repository with open-source 3D laser scans](http://kos.informatik.uni-osnabrueck.de/3Dscans/)  
It defenitely works with dataset #26  
It must work with datasets #25 and #24   
Maybe it works with datasets #23, #22, #21  
With some corrections it can work with #21, #20 and #17  
The core of this utility is based on the algorithm from 3DToolKit. While working with point clouds from Repository I tried to compile and install 3DTK but failed. I just found the way it makes rotatation matrix from Euler angles in the programm code of 3DTK and realized this algorothm in this friendly simple utility for point cloud rotation. After proccessing a point cloud through this algorithm you can load it to CloudCompare or another software for pre-proccessing.  
//LINK TO THE 3DTK//.   
This utility was designed for working with cloud number 26.  
//Does it works with other clouds from the Robotics repository?//  
