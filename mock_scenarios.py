from typing import Dict, Any, List

SCENARIOS: Dict[str, Dict[str, Any]] = {
    "ramesh_mason": {
        "id": "ramesh_mason",
        "title": "रमेश कुमार (राजमिस्त्री / निर्माण मजदूर - नोएडा सेक्टर 62)",
        "subtitle": "निर्माण क्षेत्र: 2 दिन की झूठी गैरहाजिरी और 5 घंटे का दबाया गया ओवरटाइम",
        "worker_name": "रमेश कुमार",
        "thekedar_name": "राजेश ठेकेदार",
        "trade": "राजमिस्त्री (Mason)",
        "daily_rate": 650.0,
        "location": "नोएडा सेक्टर 62, कमर्शियल प्लाजा साइट",
        "language_code": "hi-IN",
        "sample_audio_path": "/static/samples/sample_audio_ramesh.mp3",
        "sample_diary_image": "/static/samples/sample_diary_ramesh.png",
        "voice_logs": [
            {
                "date": "10-10",
                "regular_hours": 8,
                "overtime_hours": 0,
                "advance_taken": 0,
                "site_location": "सेक्टर 62",
                "summary_hindi": "10 अक्टूबर: सुबह 9 से शाम 5 तक बेसमेंट का काम किया। कोई एडवांस नहीं लिया।"
            },
            {
                "date": "11-10",
                "regular_hours": 8,
                "overtime_hours": 1,
                "advance_taken": 0,
                "site_location": "सेक्टर 62",
                "summary_hindi": "11 अक्टूबर: पिलर ढलाई में 1 घंटा ज्यादा लगा, कुल 9 घंटे काम।"
            },
            {
                "date": "12-10",
                "regular_hours": 8,
                "overtime_hours": 2,
                "advance_taken": 200,
                "site_location": "सेक्टर 62",
                "summary_hindi": "12 अक्टूबर: छत ढलाई पर 2 घंटे ओवरटाइम किया। दोपहर में ₹200 चाय-नाश्ता खर्चा लिया।"
            },
            {
                "date": "13-10",
                "regular_hours": 8,
                "overtime_hours": 0,
                "advance_taken": 0,
                "site_location": "सेक्टर 62",
                "summary_hindi": "13 अक्टूबर: पूरा दिन दीवार की चिनाई की। ठेकेदार ने खुद काम देखा था।"
            },
            {
                "date": "14-10",
                "regular_hours": 8,
                "overtime_hours": 1,
                "advance_taken": 0,
                "site_location": "सेक्टर 62",
                "summary_hindi": "14 अक्टूबर: प्लास्टर का काम किया, शाम को 1 घंटा लेट तक काम चला।"
            },
            {
                "date": "15-10",
                "regular_hours": 8,
                "overtime_hours": 2,
                "advance_taken": 0,
                "site_location": "सेक्टर 62",
                "summary_hindi": "15 अक्टूबर: लिफ्ट शाफ्ट की चिनाई पूरी की, 2 घंटे एक्स्ट्रा काम हुआ।"
            },
            {
                "date": "16-10",
                "regular_hours": 8,
                "overtime_hours": 0,
                "advance_taken": 500,
                "site_location": "सेक्टर 62",
                "summary_hindi": "16 अक्टूबर: पूरे 8 घंटे काम किया। घर भेजने के लिए ₹500 नगद एडवांस लिया।"
            }
        ],
        "thekedar_diary": [
            {"date": "10-10", "status": "Present", "overtime_hours": 0, "advance_inr": 0, "thekedar_remark": "फाउंडेशन"},
            {"date": "11-10", "status": "Present", "overtime_hours": 1, "advance_inr": 0, "thekedar_remark": "पिलर ढलाई"},
            {"date": "12-10", "status": "Present", "overtime_hours": 0, "advance_inr": 200, "thekedar_remark": "छत (OT काटा)"},
            {"date": "13-10", "status": "Absent", "overtime_hours": 0, "advance_inr": 0, "thekedar_remark": "बीमार बोलकर नहीं आया (झूठ)"},
            {"date": "14-10", "status": "Present", "overtime_hours": 0, "advance_inr": 0, "thekedar_remark": "दीवार चिनाई"},
            {"date": "15-10", "status": "Absent", "overtime_hours": 0, "advance_inr": 0, "thekedar_remark": "गैरहाजिर दर्ज"},
            {"date": "16-10", "status": "Present", "overtime_hours": 0, "advance_inr": 500, "thekedar_remark": "खर्चा लिया"}
        ]
    },
    "sunita_artisan": {
        "id": "sunita_artisan",
        "title": "सुनीता देवी (जरी व कसीदाकारी कारीगर - सूरत/लखनऊ)",
        "subtitle": "असंगठित हस्तशिल्प: 30 साड़ियों के पीस-रेट में ₹1,800 की मनमानी कटौती",
        "worker_name": "सुनीता देवी",
        "thekedar_name": "बंसल गारमेंट्स (सेठजी)",
        "trade": "कशीदाकारी / जरी कारीगर",
        "daily_rate": 500.0,
        "location": "सूरत टेक्सटाइल हब",
        "language_code": "hi-IN",
        "sample_audio_path": "/static/samples/sample_audio_ramesh.mp3",
        "sample_diary_image": "/static/samples/sample_diary_ramesh.png",
        "voice_logs": [
            {
                "date": "05-10 to 12-10",
                "regular_hours": 48,
                "overtime_hours": 10,
                "advance_taken": 500,
                "site_location": "वर्कशॉप रिंग रोड",
                "summary_hindi": "30 पीस भारी बनारसी दुपट्टे जरी काम पूरा करके 12 तारीख को सौंपे। ₹60 प्रति पीस तय था।"
            }
        ],
        "thekedar_diary": [
            {"date": "12-10", "status": "Delivered", "overtime_hours": 0, "advance_inr": 500, "thekedar_remark": "10 पीस में धागा ढीला बोलकर ₹600 काटा, ₹1,200 रिजेक्शन"}
        ]
    },
    "murugan_painter": {
        "id": "murugan_painter",
        "title": "के. मुरुगन (कमर्शियल पेंटर - बेंगलुरु मेट्रो साइट)",
        "subtitle": "प्रवासी मजदूर: नाइट-शिफ्ट ओवरटाइम और मनमाना ट्रांसपोर्ट किराया काटा",
        "worker_name": "के. मुरुगन",
        "thekedar_name": "शिवकुमार कांट्रेक्टर",
        "trade": "स्प्रे पेंटर (Commercial Painter)",
        "daily_rate": 750.0,
        "location": "बेंगलुरु नम्मा मेट्रो फेज 2",
        "language_code": "hi-IN",
        "sample_audio_path": "/static/samples/sample_audio_ramesh.mp3",
        "sample_diary_image": "/static/samples/sample_diary_ramesh.png",
        "voice_logs": [
            {
                "date": "08-10 to 14-10",
                "regular_hours": 48,
                "overtime_hours": 14,
                "advance_taken": 800,
                "site_location": "मेट्रो स्टेशन 14",
                "summary_hindi": "7 दिन रात की शिफ्ट में 14 घंटे भारी स्प्रे पेंटिंग का काम किया।"
            }
        ],
        "thekedar_diary": [
            {"date": "08-10 to 14-10", "status": "Present", "overtime_hours": 2, "advance_inr": 1800, "thekedar_remark": "टैम्पो किराया ₹1000 + ₹800 नगद"}
        ]
    }
}
