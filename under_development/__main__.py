from vacuum.vacuum import VACUUM
from vacuum.vacuum import main
from vacuum.modus import changeFanSpeed, changeWaterGrade
from vacuum.attachments import *

if __name__ == "__main__":
    main()

    fetchStates()

    changeFanSpeed()
    changeWaterGrade()
