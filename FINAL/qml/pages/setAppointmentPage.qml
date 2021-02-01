import QtQuick 2.15
import QtQuick.Controls 1.4





    Rectangle {
        id: rectangle
        anchors.fill: parent
        gradient: Gradient {
            GradientStop {
                position: 0
                color: "#323f54"
            }

            GradientStop {
                position: 1
                color: "#4c5568"
            }
        }
        Calendar {
            id: calendar
            x: 0
            y: 0
            width: parent.width/3
            height:parent.height/2
            frameVisible: true
            weekNumbersVisible: true
            selectedDate: new Date(2014, 0, 1)
            focus: true


        }
    }



/*##^##
Designer {
    D{i:0;autoSize:true;height:480;width:640}
}
##^##*/
