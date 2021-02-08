import QtQuick 2.15
import QtQuick.Controls 1.4
import QtQuick.LocalStorage 2.12
import QtQuick.Controls 2.15

import "../models"


Rectangle {
    id: rectangle
    color: "#323f54"
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



    Connections{
        target: backend
    }


    ListView {
        id: listView
        anchors.fill: parent
//        required SetAppointmentListModel
        model:appointmentModel
        delegate: Item {
            x : 0
            height: 125
            width: 800

            Row {
                id: setappointmentrow
                width: rectangle.width
                height: 120

                SetAppointmentModel{
                    doc_name_string:"omid"
                }


            }
        }

        ListModel {
                id: listModel

                Component.onCompleted: {
                    for (var i = 0; i < 1; i++) {
                        append(createListElement());
                    }
                }

                function createListElement() {

                    return {
                        hour: "01"
                    };
                }
            }
    }


    RoundButton {
        id: roundButton
        x: 565
        y: 405
        width: 67
        height: 67
        text: "+"
        anchors.right: parent.right
        anchors.bottom: parent.bottom
        bottomPadding: 11
        font.strikeout: false
        font.italic: true
        font.bold: true
        highlighted: true
        font.family: "Verdana"
        font.pointSize: 19
        anchors.bottomMargin: 8
        anchors.rightMargin: 8
        onClicked:
        {

            backend.openAppointment();
        }
    }
}



/*##^##
Designer {
    D{i:0;autoSize:true;formeditorZoom:0.75;height:480;width:800}
}
##^##*/
