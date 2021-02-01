import QtQuick 2.15
import QtQuick.Controls 2.15
import "../models"




    Rectangle {
        id: rectangle
        color: "#2c313c"

        gradient: Gradient {
            GradientStop {
                position: 0
                color: "#2c313c"
            }

            GradientStop {
                position: 0.53239
                color: "#323f54"
            }

            GradientStop {
                position: 1
                color: "#2d384b"
            }

        }

        ListView {
            id: listView
            anchors.bottom: parent.bottom
            anchors.fill: parent
            anchors.rightMargin: 0
            anchors.leftMargin: 0
            anchors.bottomMargin: 0
            anchors.topMargin: 0
            model: ListModel {
                ListElement {
                    name: "Grey"
                    colorCode: "grey"
                }

                ListElement {
                    name: "Red"
                    colorCode: "red"
                }

                ListElement {
                    name: "Red"
                    colorCode: "red"
                }
            }
            delegate: Item {
                x: 0
                width: 800
                height: 240

                Row {
                    id: row1
                    width: rectangle.width
                    height: parent.height

                    SavabeghModel{

                    }


                }
            }
        }


    }





/*##^##
Designer {
    D{i:0;autoSize:true;formeditorZoom:0.75;height:480;width:800}
}
##^##*/
