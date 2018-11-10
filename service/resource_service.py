from commons.utils import to_dict
from data.manager import RichTextMgr, PicMgr
from data.manager.proj import ProjRecruitPostMgr


def create_or_update_rich_text(bus_type, bus_id, title, text_type, content, sequence=0, subtitle='', rich_text_id=0):
    if rich_text_id:
        rich_text = RichTextMgr.get(rich_text_id)
        RichTextMgr.update(rich_text, title=title, sequence=sequence, rich_text=content, subtitle=subtitle)
    else:
        sequence = RichTextMgr.get_last_sequence_by_type(bus_type, bus_id, text_type) + 1
        rich_text = RichTextMgr.create(bus_type=bus_type, bus_id=bus_id, title=title, text_type=text_type,
                                       sequence=sequence, rich_text=content, subtitle=subtitle)
    if bus_type == 'post':
        ProjRecruitPostMgr.modified(bus_id)
    return to_dict(rich_text)


def delete_rich_text(rich_text_id):
    rich_text = RichTextMgr.get(rich_text_id)
    if rich_text:
        RichTextMgr.delete(rich_text)
        if rich_text.bus_type == 'post':
            ProjRecruitPostMgr.modified(rich_text.bus_id)


def create_pic(bus_type, bus_id, img_type, url, override):
    if override:
        PicMgr.clear_pic_list(bus_type, bus_id, img_type)
        sequence = 1
    else:
        sequence = PicMgr.get_last_sequence_by_type(bus_type, bus_id, img_type) + 1
    if bus_type == 'post':
        ProjRecruitPostMgr.modified(bus_id)
    return PicMgr.create(bus_type=bus_type, bus_id=bus_id, img_type=img_type, url=url, sequence=sequence)


def delete_pic(pic_id):
    pic = PicMgr.get(pic_id)
    if pic:
        PicMgr.delete(pic)
        if pic.bus_type == 'post':
            ProjRecruitPostMgr.modified(pic.bus_id)
