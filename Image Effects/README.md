## •	Motivation
  *	With the advancement in technology, photography and photo editing has gained a lot of popularity worldwide.
  *	Photo editing softwares also known as ‘Photo editors’ provide a large variety of tools to enhance your photos and style them according to your choice. 
  * This type of app offers a wide range of diverse features from cropping, controlling shutter speed, and adding filters.
  * The goal of this project is to apply photo effects to the image using machine learning software library – OpenCv. 

## Available Effects:
1.	Grayscale:
Using OpenCV and Python, an RGB color image can be converted into a pencil sketch in four simple steps:
i)	Convert the RGB color image to grayscale.
ii)	Invert the grayscale image to get a negative.
iii)	Apply a Gaussian blur to the negative from step 2.
iv)	Blend the grayscale image from step 1 with the blurred negative from step 3 using a color dodge.

2.	Cartoon:
To create a cartoon effect, we need to pay attention to two things; edge and color palette. Those are what make the differences between a photo and a cartoon. To adjust that two main components, there are four main steps that we will go through:
i)	Load image
ii)	Create edge mask
iii)	Reduce the color palette
iv)	Combine edge mask with the colored image

3.	Oil painting:
Using the function from inbuilt library ‘xphoto’  which also has several other cool functions like image in painting, white balance, image denoising, etc. 
i)	Call the ‘cv2.xphoto()’ 
ii)	Pass the parameters for the intensity of the effect to be applied.

4.	Water painting
Here, we use the stylization library function, which produces various effects, edge-aware filters, high and low contrast features. 
i)	Adjust the amount of smoothening by using sigma spatial parameter 
ii)	Adjust how the dissimilar colors within the neighborhood will be averaged using sigma range.

5.	Grayscale
Grayscaling is the process of converting an image from other color spaces e.g. RGB, CMYK, HSV, etc. to shades of gray. It varies between complete black and complete white.
i)	Use ‘cv2.cvtColor()’ to grayscale the image

6.	Blur
We use inbuilt ‘blur()’ function declared in openCV with the intensity of blurness. 


##	Features of the WebApp:
1.	Fast
2.	Efficient for applying various effects to images
3.	Adjusts image pixels wisely to produce filter
4.	Easy to use
5.	Great UI

## Steps to Use the Web Application

1.	Upload image
2.	Select which effect you want to apply
3.	Save it in local directory
