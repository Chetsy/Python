import maya.cmds as cmds
import random



cubeList = cmds.ls ( 'Mother_Cube*' )
if len ( cubeList ) > 0:
    cmds.delete ( cubeList )

result = cmds.polyCube( w=4, h=4, d=4, name='Mother_Cube#' )

#print ('result:') + str( result )

transformName = result [0]

#Number of cubes
for i in range (0, 40 ):
   
    instanceResult = cmds.instance( transformName, name=transformName + '_instance#' )

    #Random position of cubes

    #print ('instanceResult:') + str( instanceResult )
    x = random.uniform(-20.0,20.0)
    z = random.uniform(-20.0,20.0)
    y = random.uniform(-20.0,20.0)

    
    cmds.move( x, y, z, instanceResult )
    

    #Random Rotation Generation
    cmds.rotate( x, y, z, instanceResult )
    
    xRot = random.uniform (0, 360 )
    yRot = random.uniform (0, 360 )
    zRot = random.uniform (0, 360 )

    #Random Scale Generation
    scallingFactor = random.uniform( 0.3, 1.5 )



    cmds.scale( scallingFactor, scallingFactor, scallingFactor, instanceResult )


