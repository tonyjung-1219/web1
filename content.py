{
    "version": "2.0",
    "template": {
        "outputs": [
            {
                "basicCard": {
                    "title": "(설교제목)",
                    "description": "(날짜정보) + (본문 구절)",

                    "buttons": [
                        {
                            "action": "weblink",
                            "label": "동영상 실행하기",
                            "weblinkurl": "(설교 동영상)"
                        },
                        {
                            "action":  "blocid",
                            "label": "취소하기",
                            "blockid": "(풀백 블록)"
                        }
                    ]
                }
            }
        ]
    }
}
