import QtQuick 2.15

import "../models"

Rectangle {
    id : bg
    Rectangle {
        id: rectangle
        color: "#4c4e5c"
        anchors.fill: parent
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

                ChatMessageModel{
                    doc_name_string:model.display["doc_name"]
                    date_string:model.display["date"]
                    time_string:model.display["time"]
                }


            }
        }

    }

}


/*##^##
Designer {
    D{i:0;autoSize:true;height:480;width:800}
}
##^##*/
