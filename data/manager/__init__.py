from org_manager import OrgManager
from wage_manager import WageManager
from wage_raw_data_manager import WageRawDataManager
from fine_manager import FineManager
from supplier_manager import SupplierManager
from data.manager.crew.crew_level_manager import CrewLevelManager
from data.manager.crew.crew_manager import CrewManager
from data.manager.crew.crew_proj_map_manager import CrewProjMapManager

from data.manager.framework.dao_relation_map_manager import DaoRelationMapManager
from data.manager.framework.fe_configure_manager import FeConfigureManager
from data.manager.framework.org_proj_map_manager import OrgProjMapManager
from data.manager.framework.pic_manager import PicManager
from data.manager.framework.rich_text_manager import RichTextManager
from data.manager.framework.plugin_manager import PluginManager

from data.manager.dataset.dataset_manager import DatasetManager
from data.manager.dataset.dw_billboard_points_manager import DwBillboardPointsManager
from data.manager.dataset.dw_chart_points_manager import DwChartPointsManager

DaoRelationMapMgr = DaoRelationMapManager()
FeConfigureMgr = FeConfigureManager()
OrgProjMapMgr = OrgProjMapManager()
PluginMgr = PluginManager()
RichTextMgr = RichTextManager()
PicMgr = PicManager()
SupplierMgr = SupplierManager()

OrgMgr = OrgManager()
FineMgr = FineManager()
WageRawDataMgr = WageRawDataManager()
WageMgr = WageManager()
CrewMgr = CrewManager()
CrewLevelMgr = CrewLevelManager()
CrewProjMapMgr = CrewProjMapManager()

DatasetMgr = DatasetManager()
DwChartPointsMgr = DwChartPointsManager()
DwBillboardPointsMgr = DwBillboardPointsManager()