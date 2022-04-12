# -*- coding: mbcs -*-
from part import *
from material import *
from section import *
from assembly import *
from step import *
from interaction import *
from load import *
from mesh import *
from optimization import *
from job import *
from sketch import *
from visualization import *
from connectorBehavior import *
# mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
# mdb.models['Model-1'].sketches['__profile__'].Arc3Points(point1=(-10.0, 0.0), 
#     point2=(0.0, 5.0), point3=(10.0, 0.0))
# del mdb.models['Model-1'].sketches['__profile__']
def fn(h):
    mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
    mdb.models['Model-1'].sketches['__profile__'].Arc3Points(point1=(10.0, 0.0), 
        point2=(-10.0, 0.0), point3=(0.0, h))
    mdb.models['Model-1'].Part(dimensionality=THREE_D, name='Part-1', type=
        DEFORMABLE_BODY)
    mdb.models['Model-1'].parts['Part-1'].BaseShellExtrude(depth=20.0, sketch=
        mdb.models['Model-1'].sketches['__profile__'])
    del mdb.models['Model-1'].sketches['__profile__']
    mdb.models['Model-1'].Material(name='Material-1')
    mdb.models['Model-1'].materials['Material-1'].Density(table=((2.33e-24, ), ))
    mdb.models['Model-1'].materials['Material-1'].Elastic(table=((210.0, 0.3), ))
    mdb.models['Model-1'].HomogeneousSolidSection(material='Material-1', name=
        'Section-1', thickness=None)
    mdb.models['Model-1'].HomogeneousShellSection(idealization=NO_IDEALIZATION, 
        integrationRule=SIMPSON, material='Material-1', name='Section-2', 
        nodalThicknessField='', numIntPts=5, poissonDefinition=DEFAULT, 
        preIntegrate=OFF, temperature=GRADIENT, thickness=1.0, thicknessField='', 
        thicknessModulus=None, thicknessType=UNIFORM, useDensity=OFF)
    mdb.models['Model-1'].parts['Part-1'].Set(faces=
        mdb.models['Model-1'].parts['Part-1'].faces.getSequenceFromMask(('[#1 ]', 
        ), ), name='Set-1')
    mdb.models['Model-1'].parts['Part-1'].SectionAssignment(offset=0.0, 
        offsetField='', offsetType=MIDDLE_SURFACE, region=
        mdb.models['Model-1'].parts['Part-1'].sets['Set-1'], sectionName=
        'Section-2', thicknessAssignment=FROM_SECTION)
    mdb.models['Model-1'].rootAssembly.DatumCsysByDefault(CARTESIAN)
    mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Part-1-1', 
        part=mdb.models['Model-1'].parts['Part-1'])
    mdb.models['Model-1'].StaticStep(name='Step-1', previous='Initial')
    mdb.models['Model-1'].Gravity(comp2=-9.81, createStepName='Step-1', 
        distributionType=UNIFORM, field='', name='Load-1')
    mdb.models['Model-1'].parts['Part-1'].seedPart(deviationFactor=0.1, 
        minSizeFactor=0.1, size=1.0)
    mdb.models['Model-1'].parts['Part-1'].generateMesh()
    mdb.models['Model-1'].rootAssembly.regenerate()
    mdb.Job(atTime=None, contactPrint=OFF, description='', echoPrint=OFF, 
        explicitPrecision=SINGLE, getMemoryFromAnalysis=True, historyPrint=OFF, 
        memory=90, memoryUnits=PERCENTAGE, model='Model-1', modelPrint=OFF, 
        multiprocessingMode=DEFAULT, name='Job-2', nodalOutputPrecision=SINGLE, 
        numCpus=1, numGPUs=0, queue=None, resultsFormat=ODB, scratch='', type=
        ANALYSIS, userSubroutine='', waitHours=0, waitMinutes=0)
    mdb.jobs['Job-2'].submit(consistencyChecking=OFF)
    mdb.jobs['Job-2']._Message(STARTED, {'phase': BATCHPRE_PHASE, 
        'clientHost': 'DESKTOP-UE48J1T', 'handle': 0, 'jobName': 'Job-2'})
    mdb.jobs['Job-2']._Message(ODB_FILE, {'phase': BATCHPRE_PHASE, 
        'file': 'E:\\george\\Job-2.odb', 'jobName': 'Job-2'})
    mdb.jobs['Job-2']._Message(COMPLETED, {'phase': BATCHPRE_PHASE, 
        'message': 'Analysis phase complete', 'jobName': 'Job-2'})
    mdb.jobs['Job-2']._Message(STARTED, {'phase': STANDARD_PHASE, 
        'clientHost': 'DESKTOP-UE48J1T', 'handle': 8460, 'jobName': 'Job-2'})
    mdb.jobs['Job-2']._Message(STEP, {'phase': STANDARD_PHASE, 'stepId': 1, 
        'jobName': 'Job-2'})
    mdb.jobs['Job-2']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
        'frame': 0, 'jobName': 'Job-2'})
    mdb.jobs['Job-2']._Message(MEMORY_ESTIMATE, {'phase': STANDARD_PHASE, 
        'jobName': 'Job-2', 'memory': 36.0})
    mdb.jobs['Job-2']._Message(PHYSICAL_MEMORY, {'phase': STANDARD_PHASE, 
        'physical_memory': 32623.0, 'jobName': 'Job-2'})
    mdb.jobs['Job-2']._Message(MINIMUM_MEMORY, {'minimum_memory': 23.0, 
        'phase': STANDARD_PHASE, 'jobName': 'Job-2'})
    mdb.jobs['Job-2']._Message(WARNING, {'phase': STANDARD_PHASE, 
        'message': 'Solver problem. Numerical singularity when processing node PART-1-1.145 D.O.F. 1 ratio = 1.01920E+15.', 
        'jobName': 'Job-2'})
    mdb.jobs['Job-2']._Message(WARNING, {'phase': STANDARD_PHASE, 
        'message': 'Solver problem. Numerical singularity when processing node PART-1-1.145 D.O.F. 2 ratio = 910.703E+12  .', 
        'jobName': 'Job-2'})
    mdb.jobs['Job-2']._Message(WARNING, {'phase': STANDARD_PHASE, 
        'message': 'Solver problem. Numerical singularity when processing node PART-1-1.145 D.O.F. 3 ratio = 18.6541E+12 .', 
        'jobName': 'Job-2'})
    mdb.jobs['Job-2']._Message(WARNING, {'phase': STANDARD_PHASE, 
        'message': 'Solver problem. Numerical singularity when processing node PART-1-1.145 D.O.F. 4 ratio = 138.614E+09  .', 
        'jobName': 'Job-2'})
    mdb.jobs['Job-2']._Message(WARNING, {'phase': STANDARD_PHASE, 
        'message': 'Solver problem. Numerical singularity when processing node PART-1-1.145 D.O.F. 5 ratio = 7.70443E+09.', 
        'jobName': 'Job-2'})
    mdb.jobs['Job-2']._Message(WARNING, {'phase': STANDARD_PHASE, 
        'message': 'Solver problem. Numerical singularity when processing node PART-1-1.145 D.O.F. 6 ratio = 10.4279E+09 .', 
        'jobName': 'Job-2'})
    mdb.jobs['Job-2']._Message(WARNING, {'phase': STANDARD_PHASE, 
        'message': 'There is zero FORCE everywhere in the model based on the default criterion. please check the value of the average FORCE during the current iteration to verify that the FORCE is small enough to be treated as zero. if not, please use the solution controls to reset the criterion for zero FORCE.', 
        'jobName': 'Job-2'})
    mdb.jobs['Job-2']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
        'frame': 1, 'jobName': 'Job-2'})
    mdb.jobs['Job-2']._Message(STATUS, {'totalTime': 1.0, 'attempts': 1, 
        'timeIncrement': 1.0, 'increment': 1, 'stepTime': 1.0, 'step': 1, 
        'jobName': 'Job-2', 'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 
        'equilibrium': 1})
    mdb.jobs['Job-2']._Message(END_STEP, {'phase': STANDARD_PHASE, 'stepId': 1, 
        'jobName': 'Job-2'})
    mdb.jobs['Job-2']._Message(COMPLETED, {'phase': STANDARD_PHASE, 
        'message': 'Analysis phase complete', 'jobName': 'Job-2'})
    mdb.jobs['Job-2']._Message(JOB_COMPLETED, {'time': 'Fri Apr  1 18:13:27 2022', 
        'jobName': 'Job-2'})
    mdb.models['Model-1'].rootAssembly.Set(edges=
        mdb.models['Model-1'].rootAssembly.instances['Part-1-1'].edges.getSequenceFromMask(
        ('[#a ]', ), ), name='Set-1')
    mdb.models['Model-1'].EncastreBC(createStepName='Step-1', localCsys=None, name=
        'BC-1', region=mdb.models['Model-1'].rootAssembly.sets['Set-1'])
    mdb.models['Model-1'].boundaryConditions['BC-1'].move('Step-1', 'Initial')
    mdb.Job(atTime=None, contactPrint=OFF, description='', echoPrint=OFF, 
        explicitPrecision=SINGLE, getMemoryFromAnalysis=True, historyPrint=OFF, 
        memory=90, memoryUnits=PERCENTAGE, model='Model-1', modelPrint=OFF, 
        multiprocessingMode=DEFAULT, name='Job-3', nodalOutputPrecision=SINGLE, 
        numCpus=1, numGPUs=0, queue=None, resultsFormat=ODB, scratch='', type=
        ANALYSIS, userSubroutine='', waitHours=0, waitMinutes=0)
    mdb.jobs['Job-3'].submit(consistencyChecking=OFF)
    mdb.jobs['Job-3']._Message(STARTED, {'phase': BATCHPRE_PHASE, 
        'clientHost': 'DESKTOP-UE48J1T', 'handle': 0, 'jobName': 'Job-3'})
    mdb.jobs['Job-3']._Message(ODB_FILE, {'phase': BATCHPRE_PHASE, 
        'file': 'E:\\george\\Job-3.odb', 'jobName': 'Job-3'})
    mdb.jobs['Job-3']._Message(COMPLETED, {'phase': BATCHPRE_PHASE, 
        'message': 'Analysis phase complete', 'jobName': 'Job-3'})
    mdb.jobs['Job-3']._Message(STARTED, {'phase': STANDARD_PHASE, 
        'clientHost': 'DESKTOP-UE48J1T', 'handle': 14268, 'jobName': 'Job-3'})
    mdb.jobs['Job-3']._Message(STEP, {'phase': STANDARD_PHASE, 'stepId': 1, 
        'jobName': 'Job-3'})
    mdb.jobs['Job-3']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
        'frame': 0, 'jobName': 'Job-3'})
    mdb.jobs['Job-3']._Message(MEMORY_ESTIMATE, {'phase': STANDARD_PHASE, 
        'jobName': 'Job-3', 'memory': 36.0})
    mdb.jobs['Job-3']._Message(PHYSICAL_MEMORY, {'phase': STANDARD_PHASE, 
        'physical_memory': 32623.0, 'jobName': 'Job-3'})
    mdb.jobs['Job-3']._Message(MINIMUM_MEMORY, {'minimum_memory': 23.0, 
        'phase': STANDARD_PHASE, 'jobName': 'Job-3'})
    mdb.jobs['Job-3']._Message(WARNING, {'phase': STANDARD_PHASE, 
        'message': 'There is zero FORCE everywhere in the model based on the default criterion. please check the value of the average FORCE during the current iteration to verify that the FORCE is small enough to be treated as zero. if not, please use the solution controls to reset the criterion for zero FORCE.', 
        'jobName': 'Job-3'})
    mdb.jobs['Job-3']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
        'frame': 1, 'jobName': 'Job-3'})
    mdb.jobs['Job-3']._Message(STATUS, {'totalTime': 1.0, 'attempts': 1, 
        'timeIncrement': 1.0, 'increment': 1, 'stepTime': 1.0, 'step': 1, 
        'jobName': 'Job-3', 'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 
        'equilibrium': 1})
    mdb.jobs['Job-3']._Message(END_STEP, {'phase': STANDARD_PHASE, 'stepId': 1, 
        'jobName': 'Job-3'})
    mdb.jobs['Job-3']._Message(COMPLETED, {'phase': STANDARD_PHASE, 
        'message': 'Analysis phase complete', 'jobName': 'Job-3'})
    mdb.jobs['Job-3']._Message(JOB_COMPLETED, {'time': 'Fri Apr  1 18:15:43 2022', 
        'jobName': 'Job-3'})
    # Save by P190027ME on 2022_04_01-18.26.26; build 2020 2019_09_13-23.19.31 163176

def main():
    t = 1.0
    for i in range(10):
        fn(1.0)

if __name__=="__main__":
    main()