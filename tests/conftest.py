import itertools
import mock
import pytest
from .cliverifier import CliVerifier
from .robotdoc import RobotDoc


@pytest.fixture
def cliverifier(script_runner, docspec, mock_crldocbuilder, robotdoc, resource):
    c = CliVerifier()
    c.set_script_runner(script_runner)
    c.set_docspec(docspec)
    c.set_mock_crldocbuilder(mock_crldocbuilder)
    c.set_robotdoc(robotdoc)
    c.set_resource(resource)
    return c


DOCSPECS = ['all', 'builtin', 'api', 'crl']
DOCSPEC_COMB = [set(c) for r in range(len(DOCSPECS))
                for c in itertools.combinations(DOCSPECS, r)]


@pytest.fixture(params=DOCSPEC_COMB)
def docspec(request):
    return request.param


@pytest.fixture()
def mock_crldocbuilder():
    with mock.patch('crl.doc.cmdline.CRLDocBuilder') as p:
        yield p


ROOT_PATHS = [[], [['root']], [['root0'], ['root1']], [['root'], ['parent', 'child']]]


@pytest.fixture(params=ROOT_PATHS)
def robotdoc(request, tmpdir):
    with RobotDoc(tmpdir=tmpdir, rootpaths=request.param).ctx() as r:
        yield r


RESOURCES = [['resource{}'.format(i) for i in range(j)] for j in range(3)]


@pytest.fixture(params=RESOURCES)
def resource(request):
    return request.param
