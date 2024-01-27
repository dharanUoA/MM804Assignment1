import vtk

reader = vtk.vtkSTLReader()
reader.SetFileName("teapot.stl")

# Get the number of points (vertices)
# reader.Update()
# polydata = reader.GetOutput()
# num_vertices = polydata.GetNumberOfPoints()
# print(num_vertices)

normals = vtk.vtkPolyDataNormals()
normals.SetInputConnection(reader.GetOutputPort())

# No shading or texture for actor 1
mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(reader.GetOutputPort())
actor1 = vtk.vtkActor()
actor1.SetMapper(mapper)
actor1.RotateX(270)
properties = actor1.GetProperty()
properties.SetColor(1,1,0)
properties.SetRepresentationToWireframe()

# Flat shading for actor 2
mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(normals.GetOutputPort())
actor2 = vtk.vtkActor()
actor2.SetMapper(mapper)
actor2.RotateX(270)
properties = actor2.GetProperty()
properties.SetInterpolationToFlat()
properties.SetColor(1,1,0)
properties.SetDiffuse(0.8)
properties.SetSpecular(0.5)
properties.SetSpecularPower(30.0)

# Gouraud shading for actor 3
mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(normals.GetOutputPort())
actor3 = vtk.vtkActor()
actor3.SetMapper(mapper)
actor3.RotateX(270)
properties = actor3.GetProperty()
properties.SetInterpolationToGouraud()
properties.SetColor(1,1,0)
properties.SetDiffuse(0.8) 
properties.SetAmbient(0.3) 
properties.SetSpecular(0.5)
properties.SetSpecularPower(30.0)

# Phong shading for actor 4
mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(normals.GetOutputPort())
actor4 = vtk.vtkActor()
actor4.SetMapper(mapper)
actor4.RotateX(270)
properties = actor4.GetProperty()
properties.SetInterpolationToPhong()
properties.SetColor(1, 1, 0)
properties.SetDiffuse(0.8)
properties.SetAmbient(0.3)
properties.SetSpecular(0.5)
properties.SetSpecularPower(30.0)

# create 4 renderers for each section
renderer1 = vtk.vtkRenderer()
renderer1.SetViewport(0, 0.5, 0.5, 1) # top left
renderer1.AddActor(actor1)

renderer2 = vtk.vtkRenderer()
renderer2.SetViewport(0.5, 0.5, 1, 1) # top right
renderer2.AddActor(actor2)

renderer3 = vtk.vtkRenderer()
renderer3.SetViewport(0, 0, 0.5, 0.5) # bottom left
renderer3.AddActor(actor3)

renderer4 = vtk.vtkRenderer()
renderer4.SetViewport(0.5, 0, 1, 0.5) # bottom right
renderer4.AddActor(actor4)

# add all rendereres to renderer window 
renWin = vtk.vtkRenderWindow()
renWin.SetSize(600, 600)
renWin.AddRenderer(renderer1)
renWin.AddRenderer(renderer2)
renWin.AddRenderer(renderer3)
renWin.AddRenderer(renderer4)
renWin.Render()

output_to_image = True

if output_to_image:
    # write to image file
    window_to_image_filter = vtk.vtkWindowToImageFilter()
    window_to_image_filter.SetInput(renWin)
    window_to_image_filter.SetInputBufferTypeToRGB()
    window_to_image_filter.ReadFrontBufferOff()
    window_to_image_filter.Update()

    jpg_writer = vtk.vtkJPEGWriter()
    jpg_writer.SetFileName("output_image.jpg") 
    jpg_writer.SetInputConnection(window_to_image_filter.GetOutputPort())
    jpg_writer.Write()
else:
    # create interaction window
    iren = vtk.vtkRenderWindowInteractor()
    iren.SetInteractorStyle(vtk.vtkInteractorStyleTrackballActor())
    iren.SetRenderWindow(renWin)
    iren.Initialize()
    iren.Start()