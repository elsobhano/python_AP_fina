import QtQuick 2.15




Item {
    Rectangle {
        id: rectangle
        anchors.fill: parent
        gradient: Gradient {
            GradientStop {
                position: 0
                color: "#55aaff"
            }

            GradientStop {
                position: 1
                color: "#000000"
            }
        }
    }

}

/*##^##
Designer {
    D{i:0;autoSize:true;formeditorZoom:0.66;height:480;width:800}D{i:1}
}
##^##*/
